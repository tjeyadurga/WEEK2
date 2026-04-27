import streamlit as st
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


# ---------------------------------
# Streamlit UI
# ---------------------------------
st.set_page_config(page_title="Agentic RAG")
st.title("🧠 Agentic RAG Chatbot")
st.write("Upload a PDF and ask questions")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is None:
    st.info("Please upload a PDF to continue")
    st.stop()


# ---------------------------------
# Save PDF
# ---------------------------------
with open("temp.pdf", "wb") as f:
    f.write(uploaded_file.read())


# ---------------------------------
# Load & Split PDF
# ---------------------------------
loader = PyPDFLoader("temp.pdf")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
documents = splitter.split_documents(documents)


# ---------------------------------
# Embeddings & FAISS
# ---------------------------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(documents, embeddings)

st.success("PDF indexed successfully!")


# ---------------------------------
# AGENTIC LOGIC (Manual Agent)
# ---------------------------------
def agentic_rag(question: str) -> str:
    """
    Agent steps:
    1. Decide if retrieval is needed
    2. Retrieve relevant docs
    3. Compose final answer
    """

    # Step 1: Decide (simple heuristic)
    needs_retrieval = True

    context = ""
    if needs_retrieval:
        docs: List = vectorstore.similarity_search(question, k=3)
        context = "\n\n".join(d.page_content for d in docs)

    # Step 2: Generate answer (no LLM, rule-based)
    if context.strip() == "":
        return "No relevant information found in the document."

    return f"""
📄 **Answer based on retrieved PDF content**

{context}
"""


# ---------------------------------
# Ask Question
# ---------------------------------
question = st.text_input("Ask a question from the PDF")

if question:
    answer = agentic_rag(question)
    st.subheader("🤖 Agent Answer")
    st.write(answer)
