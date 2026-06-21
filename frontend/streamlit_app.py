import streamlit as st
import sys
import shutil
from pathlib import Path

# ---------------------------------
# Add backend to Python path
# ---------------------------------
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root / "backend"))

from app.graph.crag_graph import graph
from app.services.pdf_ingestion_service import (
    save_uploaded_files,
    process_uploaded_documents
)
from app.utils.config import PDF_DIR, VECTOR_DB_DIR
from app.nodes.retriever import reset_retriever

# ---------------------------------
# Page Config
# ---------------------------------
st.set_page_config(
    page_title="Agentic CRAG",
    layout="wide"
)

# ---------------------------------
# Session State Initialization
# ---------------------------------
if "processed_files" not in st.session_state:
    st.session_state.processed_files = []

# ---------------------------------
# Sidebar
# ---------------------------------
st.sidebar.header("📂 Upload PDFs")

uploaded_files = st.sidebar.file_uploader(
    "Choose PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

# ---------------------------------
# No PDFs Uploaded
# ---------------------------------
if not uploaded_files:

    pdf_path = Path(PDF_DIR)
    vector_path = Path(VECTOR_DB_DIR)

    reset_retriever()

    if pdf_path.exists():
        shutil.rmtree(pdf_path)

    if vector_path.exists():
        shutil.rmtree(vector_path)

    st.session_state.processed_files = []

# ---------------------------------
# PDFs Uploaded
# ---------------------------------
else:

    current_files = sorted(
        [file.name for file in uploaded_files]
    )

    if current_files != st.session_state.processed_files:

        with st.spinner("Processing uploaded PDFs..."):

            save_uploaded_files(
                uploaded_files,
                PDF_DIR
            )

            process_uploaded_documents()

        st.session_state.processed_files = current_files

        st.sidebar.success(
            "Documents processed successfully!"
        )

# ---------------------------------
# Main UI
# ---------------------------------
st.title("🤖 Agentic CRAG System")

query = st.text_input(
    "Ask a Question"
)

# ---------------------------------
# Ask Question
# ---------------------------------
if st.button("Ask"):

    if query.strip():

        with st.spinner("Thinking..."):

            result = graph.invoke(
                {
                    "question": query,
                    "retry_count": 0
                }
            )

        # -------------------------
        # Answer
        # -------------------------
        st.subheader("Answer")
        st.write(result["answer"])

        # -------------------------
        # Sources
        # -------------------------
        if result.get("documents"):

            st.subheader("Sources")

            shown_sources = set()

            for doc in result["documents"]:

                source = Path(
                    doc.metadata.get(
                        "source",
                        "Unknown"
                    )
                ).name

                page = (
                    doc.metadata.get(
                        "page",
                        0
                    ) + 1
                )

                key = f"{source}-{page}"

                if key not in shown_sources:

                    shown_sources.add(key)

                    st.write(
                        f"📄 {source} - Page {page}"
                    )