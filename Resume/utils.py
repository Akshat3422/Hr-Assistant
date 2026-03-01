import os
from langchain_community.vectorstores import FAISS

def create_and_save_index(docs, embedding, candidate_id):
    vector_store = FAISS.from_documents(docs, embedding)

    path = f"indexes/{candidate_id}"
    os.makedirs(path, exist_ok=True)

    vector_store.save_local(path)

    return vector_store



