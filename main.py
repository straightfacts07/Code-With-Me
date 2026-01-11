import chromadb
import uuid

cilent = chromadb.Client()

collection = cilent.create_collection(name="docs")
with open ("docs.txt","r",encoding="utf-8") as f:
    docs: list[str]=f.read().splitlines()

collection.add(
    ids=[str(uuid.uuid4()) for _ in docs],
    documents=docs,
    metadatas=[{"line":line} for line in range(len(docs))]
     
)

result=collection.query(
    query_texts=[
        "what is polymorphism?",
        "what are pointers?"
    ],
    n_results=5
)

for i, query_results in enumerate(result["documents"]):
    print(f"\nQuery{i}")
    print("\n".join(query_results))
