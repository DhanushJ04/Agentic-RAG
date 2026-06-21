from pathlib import Path
import shutil
from app.ingestion.vector_store import create_vector_store
from app.nodes.retriever import reset_retriever


def save_uploaded_files(uploaded_files, save_dir):

    save_path = Path(save_dir)

    if save_path.exists():
        shutil.rmtree(save_path)

    save_path.mkdir(
        parents=True,
        exist_ok=True
    )

    for uploaded_file in uploaded_files:

        destination = (
            save_path /
            uploaded_file.name
        )

        with open(destination, "wb") as f:
            f.write(
                uploaded_file.getbuffer()
            )


def process_uploaded_documents():

    create_vector_store()
    reset_retriever()