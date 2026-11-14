import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

# Use Pinecone's built-in inference for embeddings instead of Bedrock
pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

response = pc.inference.embed(
    model="multilingual-e5-large",
    inputs=["What is RAG application"],
    parameters={"input_type": "passage", "truncate": "END"}
)

print("Successfully generated embedding vector via Pinecone!")
print("Vector dimension:", len(response[0]["values"]))