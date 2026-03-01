import os
from unittest import loader
from dotenv import load_dotenv
from faiss import loader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq.chat_models import ChatGroq

load_dotenv()

groq_api_key=os.getenv('GROQ_API_KEY')



model=ChatGroq(api_key=groq_api_key,model="openai/gpt-oss-120b") # type: ignore
def create_and_save_index(docs, embedding, candidate_id):
    vector_store = FAISS.from_documents(docs, embedding)

    path = f"indexes/{candidate_id}"
    os.makedirs(path, exist_ok=True)

    vector_store.save_local(path)

    return vector_store

def load_documents(path:str):
    loader = PyMuPDFLoader(path)
    documents = loader.load()
    context="\n\n".join([doc.page_content for doc in documents])
    return context


def load_llm(llm:ChatGroq,prompt:ChatPromptTemplate,OutputParser):
    model_used=llm.with_structured_output(OutputParser)
    chain=prompt|model_used
    return chain
