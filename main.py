from fastapi import FastAPI
from app.api.document import router as document_router
from app.api.embedding import router as embedding_router

app = FastAPI(
    title="DocMind AI",
    version="1.0.0"
)

app.include_router(
    document_router,
    prefix="/documents",
    tags=["Documents"]
)
app.include_router(
    embedding_router, 
    prefix="/embeddings", 
    tags=["Embeddings"]
    )

@app.get("/")
def home():
    return {
        "message": "DocMind AI Running"
    }