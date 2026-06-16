from app.workflows.crag_workflow import run_crag


query = input("Enter Query: ")

result = run_crag(query)

print("\n" + "=" * 60)
print("FINAL ANSWER")
print("=" * 60)

print(result["answer"])

print("\n" + "=" * 60)
print("SOURCES")
print("=" * 60)

for doc in result["documents"]:

    print(
        doc.metadata.get("source"),
        "- Page",
        doc.metadata.get("page")
    )