from pathlib import Path

# backend folder
BASE_DIR = Path(__file__).resolve().parents[2]

PDF_DIR = BASE_DIR / "data" / "pdfs"

VECTOR_DB_DIR = BASE_DIR / "vectorstore"