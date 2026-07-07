from pathlib import Path

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class PDFPreprocessor:

    @staticmethod
    def extract_text(pdf_path: str) -> str:
        """
        Reads every page from a PDF and returns one large string.
        """

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"
        
        return text
    

    @staticmethod
    def split_text(text: str):
        
        splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1000,
            chunk_overlap=200
        )
        return splitter.split_text(text)