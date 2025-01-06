from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_core.runnables import RunnablePassthrough
import ollama
import logging
import os
from config import CHROMA_COLLECTION_NAME, EMBEDDING_MODEL

def load_pdf_data(doc_path: str):
    
    if os.path.exists(doc_path):
        loader = UnstructuredPDFLoader(file_path=doc_path)
        data = loader.load()
        logging.info("PDF Loaded successfully.")
        return data
    else:
        logging.error(f"PDF file not found at: {doc_path}")

def split_documents(data):
    """Split the PDF into chunks"""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
    chunks = splitter.split_documents(data)
    logging.info(f"PDF split into {len(chunks)} chunks.")
    return chunks

def create_vector_db(chunks):
    """Create the vector database"""
    # Pull the embedding model if not already pulled
    ollama.pull(EMBEDDING_MODEL)

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model=EMBEDDING_MODEL),
        collection_name=CHROMA_COLLECTION_NAME,
    )
    logging.info("Vector DB created successfully.")

    return vector_db

def create_retriever(vector_db, llm):
    """Create the retriever"""
    QUERY_PROMPT = PromptTemplate(
        input_variables=["question"],
        template="""You are an AI language model assistant. Your task is to generate five
        different versions of the given user question to retrieve relevant documents from
        a vector database. By generating multiple perspectives on the user question, your
        goal is to help the user overcome some of the limitations of the distance-based
        similarity search. Provide these alternative questions separated by newlines.
        Original question: {question}"""
    )

    retriever = MultiQueryRetriever.from_llm(
        vector_db.as_retriever(), llm, prompt=QUERY_PROMPT
    )

    logging.info("Retriever created successfully.")

    return retriever


def create_chain(retriever, llm):
    """Create the chain"""
    template = """Answer the question based ONLY on the following context: {context}
    Question: {question}
    """

    prompt = ChatPromptTemplate.from_template(template=template)

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    logging.info("Chain created successfully.")

    return chain