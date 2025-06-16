from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
import os
import json
from langchain_core.documents import Document

DB_DIR = "db/"
COLLECTION_NAME = "user_notes"

def get_vector_store():
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=DB_DIR,
        embedding_function=embeddings
    )
    return vector_store

def add_user_notes(user_id, notes):
    vector_store = get_vector_store()
    documents = [Document(page_content=note, metadata={"user": user_id}) for note in notes]
    ids = [f"{user_id}_{i}" for i in range(len(notes))]
    vector_store.add_documents(documents=documents, ids=ids)

def retrieve_notes(user_id, query):
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    return retriever.invoke(query)