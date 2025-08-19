import contextlib
import time
from metrics import latency, errors
@contextlib.contextmanager
def trace_llm(span_name: str = 'll_call'):
    start = time.perf_counter()
    try:
        yield
    except Exception:
        errors.inc()
        raise
    finally:
        latency.observe(time.perf_counter() - start)