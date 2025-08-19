from fastapi import APIRouter, Depends, Request
from fastapi.responses import StreamingResponse
from config import settings
from src.app.llm.openai_provider import OpenAIProvider
from src.app.guards.filters import is_blocked
from src.app.guards.rate_limit import TokenBucket, enforce_rate_limit
from src.app.telemetry.tracing import trace_llm
from redis import Redis
from src.app.rag.retrieve import Retriever