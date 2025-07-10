import os
import asyncio
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

load_dotenv()


embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


def ingest_docs():
    print("Ingesting docs")

    loader = ReadTheDocsLoader(
        path="langchain-docs/api.python.langchain.com/en/latest", encoding="ISO-8859-1"
    )
    raw_documents = loader.load()
    print(f"Loaded {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)

    print(f"Split into {len(documents)} chunks")

    for doc in documents:
        new_url = doc.metadata["source"].replace("langchain-docs", "https://")
        doc.metadata.update({"source": new_url})

    print(f"Going to add {len(documents)} documents to Pinecone")

    batch_size = 100

    for i in range(0, len(documents), batch_size):
        batch = documents[i : i + batch_size]
        PineconeVectorStore.from_documents(
            batch,
            embeddings,
            index_name=os.environ["INDEX_NAME"],
        )
        print(f"Uploaded batch {i // batch_size + 1} with {len(batch)} documents")

    print("**** Ingestion complete ****")


if __name__ == "__main__":
    ingest_docs()
