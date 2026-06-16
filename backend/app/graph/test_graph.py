from app.graph.crag_graph import graph


query = input("Enter Query: ")

result = graph.invoke(
    {
        "question": query,
        "retry_count": 0
    }
)

print("\n" + "=" * 60)
print("FINAL STATE")
print("=" * 60)

for key, value in result.items():

    print(f"\n{key}")

    print(value)