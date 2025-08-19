from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi import APIRouter, Response

latency = Histogram("llm_latency_seconds", "LLM call latency")
errors = Counter("llm_errors_total", "Total LLM errors")
tokens = Counter("llm_tokens_total", "Total tokens used", ["type"])  # prompt/completion

router = APIRouter()

@router.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)