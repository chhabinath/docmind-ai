from langchain_ollama import OllamaEmbeddings

from app.embeddings.base import EmbeddingService

from app.core.config import settings

class OllamaEmbedding(EmbeddingService):

    def __init__(self):
        self.model = OllamaEmbeddings(
            model = settings.embedding_model
        )

    def embed_query(self, query: str) -> list[float]:
        return self.model.embed_query(query)

    def embed_documents(self, documents: list[str]) -> list[list[float]]:
        return self.model.embed_documents(documents)

