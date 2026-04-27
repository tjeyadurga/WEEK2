import streamlit as st
from rag_agent import create_rag_agent

st.set_page_config(page_title="YouTube Agentic RAG")

st.title("🎥 Agentic RAG YouTube Summarizer")

youtube_url = st.text_input("Enter YouTube URL")

query = st.text_input(
    "Ask Question",
    placeholder="Example: Summarize this video"
)

if st.button("Run Agent"):

    if youtube_url and query:

        with st.spinner("Analyzing Video..."):

            try:
                agent = create_rag_agent(youtube_url)

                response = agent.invoke({
                    "messages": [
                        ("user", query)
                    ]
                })

                st.subheader("Answer:")
                st.success(response["messages"][-1].content)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter both URL and Question")
