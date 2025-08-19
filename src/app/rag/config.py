from pydantic_settings import BaseSettings
class settings(BaseSettings):
    APP_NAME: str = "llm_genai"
    ENV: str = "dev"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    LLM_PROVIDER: str = "openai"
    OPENAI_API_KEY: str | None = None
    MODEL_NAME: str = "gpt-3.5-turbo"
    EMB_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    FAISS_INDEX_PATH: str = "./data/index.faiss"
    DOC_STORE: str = "./data/chunk.parquet"
    REDIS_URL: str = "redis://redis:6379/0"
    RATE_LIMIT_RPS: float = 3.0
    PROMETHEUS_ENABLED:bool = True
    OTEL_ENABLED: bool = True
    JWT_SECRET: str = "dev-secret-change"

    class Config:
        env_file = ".env"

settings = settings()



