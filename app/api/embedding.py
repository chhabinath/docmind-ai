from fastapi import APIRouter

from app.embeddings.ollama_embedding_service import OllamaEmbedding

router = APIRouter(prefix="/embeddings", tags=["Embeddings"])

embedding_service = OllamaEmbedding()


@router.get("/test")
def test_embedding():

    query = "What is Artificial Intelligence?"

    embedding = embedding_service.embed_query(query)

    return {
        "query": query,
        "dimension": len(embedding),
        "first_10_values": embedding[:10]
    }