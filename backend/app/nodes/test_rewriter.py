from app.nodes.query_rewriter import rewrite_query


query = input("Enter Query: ")

rewritten_query = rewrite_query(query)

print("\nOriginal Query: ")
print(query)

print("\nRewritten Query: ")
print(rewritten_query)
