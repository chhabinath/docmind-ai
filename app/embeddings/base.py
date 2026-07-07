from abc import ABC, abstractmethod


class EmbeddingService(ABC):

    @abstractmethod
    def embed_query(self, query: str):
        """Generate embedding for a user query."""
        pass

    @abstractmethod
    def embed_documents(self, documents: list[str]):
        """Generate embeddings for multiple document chunks."""
        pass