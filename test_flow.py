import sys
from pathlib import Path

# Add backend to Python path
sys.path.append(str(Path(__file__).parent / "backend"))

from app.nodes.retriever import get_retriever
from app.nodes.grader import grade_documents, filter_relevant_documents

def run_test():
    retriever = get_retriever()

    # ============================================================
    # Test 1: Question answerable from PDF
    # Expected: grader should say "yes", relevant docs should exist
    # ============================================================
    query1 = "What are restrictions on holding shares in companies?"
    print("=" * 60)
    print(f"TEST 1: {query1}")
    print("=" * 60)

    docs1 = retriever.invoke(query1)
    print(f"Retrieved {len(docs1)} documents.")

    relevant1 = filter_relevant_documents(query1, docs1)
    decision1 = "yes" if relevant1 else "no"

    print(f"\nDecision: {decision1}")
    print(f"Relevant chunks: {len(relevant1)} / {len(docs1)}")
    for idx, doc in enumerate(relevant1):
        page = doc.metadata.get("page", 0) + 1
        print(f"  Relevant Doc {idx+1} (Page {page}): {doc.page_content[:150]}...")

    assert decision1 == "yes", f"FAIL: Expected 'yes' but got '{decision1}'"
    print("\n[PASS] TEST 1 PASSED\n")

    # ============================================================
    # Test 2: Question NOT answerable from PDF
    # Expected: grader should say "no"
    # ============================================================
    query2 = "what is digital banking?"
    print("=" * 60)
    print(f"TEST 2: {query2}")
    print("=" * 60)

    docs2 = retriever.invoke(query2)
    print(f"Retrieved {len(docs2)} documents.")

    relevant2 = filter_relevant_documents(query2, docs2)
    decision2 = "yes" if relevant2 else "no"

    print(f"\nDecision: {decision2}")
    print(f"Relevant chunks: {len(relevant2)} / {len(docs2)}")

    assert decision2 == "no", f"FAIL: Expected 'no' but got '{decision2}'"
    print("\n[PASS] TEST 2 PASSED\n")


    print("=" * 60)
    print("ALL TESTS PASSED")
    print("=" * 60)

if __name__ == "__main__":
    run_test()
