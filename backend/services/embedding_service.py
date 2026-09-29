"""Embedding Service with BGE-small-en-v1.5 (384d) and deterministic hashing fallback."""

import hashlib
import numpy as np
from typing import List
from backend.core.config import settings
from backend.core.logging_conf import logger
from backend.utils.pii import redact_pii

# Track degradation state
_embedding_degraded = False
_st_model = None


def get_embedding_model():
    """Lazily loads sentence transformer model or triggers fallback."""
    global _st_model, _embedding_degraded
    if _st_model is not None:
        return _st_model

    try:
        from sentence_transformers import SentenceTransformer
        # Try local cache without forced network download
        _st_model = SentenceTransformer(settings.EMBEDDING_MODEL, local_files_only=True)
        logger.info(f"Loaded embedding model: {settings.EMBEDDING_MODEL}")
        _embedding_degraded = False
        return _st_model
    except Exception as e:
        logger.warning(f"Could not load local embedding model ({e}); activating deterministic hashing fallback.")
        _embedding_degraded = True
        return None


def is_embedding_degraded() -> bool:
    return _embedding_degraded


def deterministic_hash_embedding(text: str, dim: int = 384) -> List[float]:
    """Generates a deterministic 384-dimensional unit vector using salted hashing.
    Used during offline tests or when model weights are not pre-downloaded.
    """
    words = text.lower().split()
    vector = np.zeros(dim, dtype=np.float32)
    for w in words:
        h = int(hashlib.sha256(w.encode("utf-8")).hexdigest(), 16)
        idx = h % dim
        sign = 1.0 if (h >> 8) % 2 == 0 else -1.0
        vector[idx] += sign

    norm = np.linalg.norm(vector)
    if norm > 0:
        vector = vector / norm
    else:
        vector[0] = 1.0
    return vector.tolist()


def encode_texts(texts: List[str]) -> List[List[float]]:
    """Scrubs PII and embeds a batch of texts into 384-dimensional vectors."""
    cleaned_texts = [redact_pii(t) for t in texts]
    model = get_embedding_model()

    if model is not None:
        try:
            embeddings = model.encode(cleaned_texts, batch_size=32, normalize_embeddings=True)
            return embeddings.tolist()
        except Exception as e:
            logger.error(f"Inference error with sentence transformer: {e}")

    # Fallback to deterministic hashed bag-of-words
    return [deterministic_hash_embedding(t, dim=settings.EMBEDDING_DIM) for t in cleaned_texts]
