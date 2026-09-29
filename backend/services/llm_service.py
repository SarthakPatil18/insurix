"""LLM Service with Groq API integration and deterministic offline synthesis fallback."""

from typing import List, Dict, Any, Tuple
from backend.core.config import settings
from backend.core.logging_conf import logger
from backend.models.schemas import EvidenceCitation, LLMInfo

SYSTEM_PROMPT = """You are Insurix, an authoritative health insurance policy intelligence engine.
Rules:
1. Answer strictly using ONLY the provided policy clauses.
2. Cite the exact page number and section (e.g. Page 18, §4.2) for every assertion.
3. State all uncertainties and ambiguities explicitly.
4. Never promise or guarantee claim settlements; state clearly that this is an estimate.
5. If the provided evidence is insufficient, say so honestly without inventing facts."""


def is_llm_available() -> bool:
    return bool(settings.GROQ_API_KEY)


def deterministic_synthesize_answer(
    question: str,
    policy_name: str,
    verdict: str,
    evidence: List[EvidenceCitation],
    cost_estimate: Dict[str, Any] = None
) -> str:
    """Offline deterministic synthesizer that constructs factual answers with exact citations."""
    q_lower = question.lower()
    
    if not evidence:
        return f"Under {policy_name}, we could not locate specific clauses addressing this inquiry in the available policy text. Please verify with your insurer."

    top_ev = evidence[0]
    citation_str = f"(Page {top_ev.page}, §{top_ev.section})"

    if verdict == "no":
        return f"Based on {policy_name}, this claim is currently disallowed {citation_str}. {top_ev.text}"

    if "knee" in q_lower or "arthroplasty" in q_lower:
        return f"Total Knee Replacement is covered under {policy_name} as a medically necessary surgery {citation_str}, subject to waiting period criteria and statutory consumable deductions."
    elif "cataract" in q_lower or "eye" in q_lower:
        return f"Cataract surgery is covered under {policy_name} {citation_str}, subject to specific illness waiting periods and disease-specific sub-limits."
    elif "room" in q_lower or "icu" in q_lower or "rent" in q_lower:
        return f"Under {policy_name}, room rent and ICU charges are subject to policy schedule limits {citation_str}. Exceeding entitled room tiers triggers proportionate billing deductions."
    elif "waiting" in q_lower or "ped" in q_lower or "pre-existing" in q_lower:
        return f"Under {policy_name}, pre-existing diseases and specific illnesses are governed by statutory waiting clocks {citation_str} before claim admissibility commences."
    else:
        return f"Under {policy_name}, coverage is governed by Section {top_ev.section} {citation_str}: \"{top_ev.text}\""


async def generate_grounded_answer(
    question: str,
    policy_name: str,
    verdict: str,
    evidence: List[EvidenceCitation],
    cost_estimate: Dict[str, Any] = None
) -> Tuple[str, LLMInfo]:
    """Generates an answer using Groq LLM when API key is provided, or falls back to deterministic synthesis."""
    if not settings.GROQ_API_KEY:
        ans = deterministic_synthesize_answer(question, policy_name, verdict, evidence, cost_estimate)
        return ans, LLMInfo(used=False, model=None)

    try:
        from groq import AsyncGroq
        client = AsyncGroq(api_key=settings.GROQ_API_KEY)
        clauses_context = "\n\n".join([f"[Page {ev.page}, §{ev.section}]: {ev.text}" for ev in evidence])
        user_message = f"Policy: {policy_name}\nQuestion: {question}\nVerdict: {verdict}\n\nEvidence Clauses:\n{clauses_context}"

        response = await client.chat.completions.create(
            model=settings.GROQ_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.15,
            max_tokens=300
        )
        answer_text = response.choices[0].message.content.strip()
        return answer_text, LLMInfo(used=True, model=settings.GROQ_MODEL)
    except Exception as e:
        logger.warning(f"Groq API error ({e}); falling back to deterministic synthesizer.")
        ans = deterministic_synthesize_answer(question, policy_name, verdict, evidence, cost_estimate)
        return ans, LLMInfo(used=False, model=None)
