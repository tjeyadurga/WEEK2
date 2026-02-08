import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="PDF RAG Chatbot")
st.title("📄 PDF RAG Chatbot (No API Key)")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    pages = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    documents = text_splitter.split_documents(pages)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(documents, embeddings)

    st.success("PDF processed successfully!")

    query = st.text_input("Ask a question from the PDF")

    if query:
        results = vectorstore.similarity_search(query, k=3)

        st.subheader("📌 Answer from PDF")
        for i, doc in enumerate(results, 1):
            st.write(f"**Result {i}:**")
            st.write(doc.page_content)
