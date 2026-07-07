from fastapi import APIRouter, UploadFile, File
from pathlib import Path
from app.utils.pdf_processor import PDFPreprocessor

from app.services.document_service import DocumentService

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    return DocumentService.save_file(file)

@router.get("/test")
async def test_pdf():

    pdf_files = list(Path("uploads").glob("*.pdf"))

    if not pdf_files:
        return {"message": "No PDF found in uploads folder"}

    pdf_path = pdf_files[0]

    text = PDFPreprocessor.extract_text(str(pdf_path))

    chunks = PDFPreprocessor.split_text(text)

    return {
        "filename": pdf_path.name,
        "total_characters": len(text),
        "total_chunks": len(chunks),
        "first_chunk": chunks[0] if chunks else "No chunks generated"
    }