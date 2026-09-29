"""Hybrid Vector Search (Dense Cosine + Sparse BM25 / ts_rank + Reciprocal Rank Fusion)."""

import numpy as np
from typing import List, Dict, Any, Optional
from rank_bm25 import BM25Okapi

from backend.core.config import settings
from backend.core.logging_conf import logger
from backend.models.schemas import EvidenceCitation
from backend.services.embedding_service import encode_texts

# In-memory document & vector store for test runs / non-pgvector environments
_memory_store: Dict[str, List[Dict[str, Any]]] = {}


def register_in_memory_chunks(policy_id: str, chunks: List[Dict[str, Any]]):
    """Registers policy chunks in the in-memory store for instant vector and keyword retrieval."""
    _memory_store[policy_id] = chunks


def get_in_memory_chunks(policy_id: str) -> List[Dict[str, Any]]:
    return _memory_store.get(policy_id, [])


def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    a = np.array(v1, dtype=np.float32)
    b = np.array(v2, dtype=np.float32)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))


def reciprocal_rank_fusion(
    dense_ranks: List[str],
    sparse_ranks: List[str],
    k: int = 60
) -> Dict[str, float]:
    """Combines dense and sparse ranked lists using RRF score = sum(1 / (k + rank))."""
    scores: Dict[str, float] = {}

    for rank, doc_id in enumerate(dense_ranks):
        scores[doc_id] = scores.get(doc_id, 0.0) + (1.0 / (k + rank + 1))

    for rank, doc_id in enumerate(sparse_ranks):
        scores[doc_id] = scores.get(doc_id, 0.0) + (1.0 / (k + rank + 1))

    return scores


def hybrid_search(
    query: str,
    policy_id: str,
    top_k: int = 5,
    threshold: float = 0.45
) -> List[EvidenceCitation]:
    """Performs dense cosine + sparse BM25 retrieval fused with RRF, with exclusion guarantee."""
    chunks = get_in_memory_chunks(policy_id)
    if not chunks:
        return []

    # 1. Dense search
    query_vector = encode_texts([query])[0]
    dense_scores = []
    for idx, c in enumerate(chunks):
        c_vec = c.get("embedding")
        if c_vec is None:
            c_vec = encode_texts([c["text"]])[0]
            c["embedding"] = c_vec
        score = cosine_similarity(query_vector, c_vec)
        dense_scores.append((str(idx), score))
    dense_scores.sort(key=lambda x: x[1], reverse=True)
    dense_top8 = [item[0] for item in dense_scores[:8]]

    # 2. Sparse BM25 search
    corpus = [c["text"].lower().split() for c in chunks]
    bm25 = BM25Okapi(corpus)
    tokenized_query = query.lower().split()
    sparse_scores = bm25.get_scores(tokenized_query)
    sparse_ranked = sorted(enumerate(sparse_scores), key=lambda x: x[1], reverse=True)
    sparse_top8 = [str(item[0]) for item in sparse_ranked[:8]]

    # 3. Reciprocal Rank Fusion
    rrf_scores = reciprocal_rank_fusion(dense_top8, sparse_top8, k=settings.RRF_K)
    sorted_doc_ids = sorted(rrf_scores.keys(), key=lambda d_id: rrf_scores[d_id], reverse=True)

    results: List[EvidenceCitation] = []
    has_exclusion = False

    for doc_id_str in sorted_doc_ids[:top_k]:
        idx = int(doc_id_str)
        chunk = chunks[idx]
        rrf_val = rrf_scores[doc_id_str]
        # Multiply by 100 for presentation score (e.g. 27.0)
        pres_score = round(rrf_val * 1000, 1)

        is_excl = "exclu" in chunk.get("heading", "").lower() or "excl" in chunk.get("section", "").lower()
        if is_excl:
            has_exclusion = True

        results.append(
            EvidenceCitation(
                text=chunk["text"],
                page=chunk.get("page", 1),
                section=chunk.get("section", "1.0"),
                score=pres_score,
                policy_id=policy_id
            )
        )

    # 4. Exclusion Guarantee: if retrieved items grant coverage, ensure exclusion clause is present
    if not has_exclusion:
        for c in chunks:
            text_lower = c["text"].lower()
            if ("not cover" in text_lower or "exclusion" in text_lower or "waiting period" in text_lower) and any(w in text_lower for w in tokenized_query if len(w) > 3):
                results.append(
                    EvidenceCitation(
                        text=c["text"],
                        page=c.get("page", 1),
                        section=c.get("section", "Excl"),
                        score=15.0,
                        policy_id=policy_id
                    )
                )
                break

    return results
