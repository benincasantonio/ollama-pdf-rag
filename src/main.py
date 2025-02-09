from config import MODEL_NAME, DOC_PATH, CHROMA_PERSIST_DIRECTORY
from pdf_rag import (
    load_pdf_data,
    split_documents,
    create_vector_db_persisted,
    create_retriever,
    create_chain,
)
import logging
from langchain_ollama import ChatOllama

logging.basicConfig(level=logging.INFO)


def main():
    """Load and process PDF Document"""

    prompt = input("Enter your question: ")

    if not prompt.strip():
        print("Please enter a question to get started.")
        return

    data = load_pdf_data(DOC_PATH)

    if data is None:
        return

    chunks = split_documents(data)

    vector_db = create_vector_db_persisted(
        chunks=chunks, persist_directory=CHROMA_PERSIST_DIRECTORY
    )

    llm = ChatOllama(model=MODEL_NAME)

    retriever = create_retriever(vector_db, llm)

    chain = create_chain(retriever, llm)

    # res = chain.invoke("What is the purpose of the document?")
    # res = chain.invoke("Give me a detiled summary of the document?")

    res = chain.invoke(prompt)
    print("Response: ")
    print(res)


if __name__ == "__main__":
    main()
