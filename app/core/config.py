from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_name: str = "DocMind AI"
    app_version: str = "1.0.0"

    ollama_base_url: str = "http://localhost:11434"

    embedding_model: str = "nomic-embed-text"
    llm_model: str = "qwen2.5:3b"

    chunk_size: int = 1000
    chunk_overlap: int = 200

    top_k: int = 5

    upload_dir: str = "uploads"
    chroma_db_dir: str = "chroma_db"

    class Config:
        env_file = ".env"


settings = Settings()