import os
import streamlit as st
from dotenv import load_dotenv

from langchain_community.utilities import SerpAPIWrapper

# Load environment variables
load_dotenv()

# Streamlit UI
st.set_page_config(page_title="Simple Email Writer", page_icon="📧")
st.title("📧 Simple Email Writer")
st.write("Streamlit + LangChain + SERP API (No GPT)")

# User Inputs
purpose = st.text_area(
    "Email Purpose",
    placeholder="Example: Request leave for 2 days"
)

tone = st.selectbox(
    "Email Tone",
    ["Professional", "Formal", "Friendly"]
)

search_query = st.text_input(
    "Optional Search Context",
    placeholder="Example: Company policy on leave"
)

sender_name = st.text_input("Your Name")

# SERP API (LangChain utility)
search = SerpAPIWrapper()

web_context = ""
if search_query:
    with st.spinner("Fetching information from web..."):
        web_context = search.run(search_query)

# Simple Email Generator (Template-based)
def generate_email(purpose, tone, context, sender):
    if tone == "Friendly":
        greeting = "Hi,"
        closing = "Best regards"
    elif tone == "Formal":
        greeting = "Respected Sir/Madam,"
        closing = "Yours sincerely"
    else:
        greeting = "Dear Sir/Madam,"
        closing = "Sincerely"

    email = f"""
{greeting}

I hope this email finds you well.

I am writing to you regarding the following matter:

{purpose}

{f"Additional information:\n{context}" if context else ""}

Please let me know if any further details are required.

{closing},
{sender}
"""
    return email.strip()

# Generate Button
if st.button("Generate Email"):
    if not purpose or not sender_name:
        st.warning("Please enter email purpose and your name.")
    else:
        email = generate_email(
            purpose=purpose,
            tone=tone,
            context=web_context,
            sender=sender_name
        )

        st.subheader("✉️ Generated Email")
        st.text_area("Email Content", email, height=300)
