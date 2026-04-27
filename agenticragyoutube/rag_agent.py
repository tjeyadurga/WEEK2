import re
from dotenv import load_dotenv

from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent

load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",   # cheaper for automation
    temperature=0
)

def get_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def create_rag_agent(youtube_url):

    video_id = get_video_id(youtube_url)

    yt = YouTubeTranscriptApi()
    transcript = yt.fetch(video_id)

    full_text = " ".join([t.text for t in transcript])

    docs = [Document(page_content=full_text)]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    splits = splitter.split_documents(docs)

    vectorstore = FAISS.from_documents(
        splits,
        OpenAIEmbeddings()
    )

    retriever = vectorstore.as_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    @tool
    def youtube_qa_tool(question: str) -> str:
        """Answer questions from YouTube transcript"""
        return qa_chain.run(question)

    prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a YouTube video summarizer. "
     "You MUST use youtube_qa_tool to answer any question about the video. "
     "Do NOT answer from your own knowledge. "
     "Always use the tool."),
    ("placeholder", "{messages}")
])


    agent = create_react_agent(
        llm,
        tools=[youtube_qa_tool],
        prompt=prompt
    )

    return agent
