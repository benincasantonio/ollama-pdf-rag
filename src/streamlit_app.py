import streamlit as st
from pdf_rag import load_pdf_data, split_documents, create_vector_db_persisted, create_retriever, create_chain
from config import MODEL_NAME, DOC_PATH, CHROMA_PERSIST_DIRECTORY
from langchain_ollama import ChatOllama

@st.cache_resource
def load_vector_db():
    data = load_pdf_data(DOC_PATH)
                    
    if(data is None):
        st.error("PDF file not found at: " + DOC_PATH)
        return
    
    chunks = split_documents(data)

    return create_vector_db_persisted(chunks=chunks, persist_directory=CHROMA_PERSIST_DIRECTORY)

def main():
    """Load and process PDF Document"""

    st.title("Ollama PDF RAG")

    question = st.text_area("Enter the question", "");


    if st.button("Process"):
        with st.spinner("Processing..."):

            if question:
                try:                    
                    vector_db = load_vector_db()
                    
                    llm = ChatOllama(model=MODEL_NAME)

                    retriever = create_retriever(vector_db, llm)
                    
                    chain = create_chain(retriever, llm)

                    res = chain.invoke(question)

                    st.markdown("**Assistant:**")
                    st.write(res)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.info("Please enter a question to get started.")


if __name__ == "__main__":
    main()