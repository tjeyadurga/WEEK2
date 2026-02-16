🧠 Generative AI Learning Repository

A hands-on learning repository to explore Generative AI (GenAI) concepts and build real-world AI-powered automation solutions using Python and Large Language Models (LLMs).

📖 Table of Contents

About the Project

Objectives

Tech Stack

Project Structure

Getting Started

API Configuration

Usage

Automation Practice Modules

Learning Outcomes

Future Scope

Contributing

License

📌 About the Project

Generative AI enables machines to generate content such as text, code, and automation workflows using trained deep learning models.

This repository is created to:

Learn GenAI fundamentals

Integrate AI APIs with Python

Automate web applications using Selenium

Build AI-powered RPA workflows

Implement Retrieval-Augmented Generation (RAG)

Develop Agentic AI applications

🎯 Objectives

Understand LLM-based applications

Learn Prompt Engineering

Build AI-integrated automation scripts

Create intelligent testing workflows

Implement AI Agents for RPA tasks

🛠️ Tech Stack
Technology	Description
Python	Programming Language
OpenAI API	LLM Integration
Selenium	Web Automation
LangChain	LLM Framework
GitHub	Version Control
VS Code	Development Environment
📂 Project Structure
genai-learning/
│
├── prompts/
├── openai-integration/
├── selenium-automation/
├── rag-system/
├── agentic-ai/
└── README.md
⚙️ Getting Started
1. Clone the Repository
git clone https://github.com/your-username/genai-learning.git
cd genai-learning
2. Install Required Libraries
pip install openai selenium langchain
🔑 API Configuration
Generate OpenAI API Key

Visit:

https://platform.openai.com/api-keys

Set Environment Variable (Windows)
setx OPENAI_API_KEY "your_api_key_here"

Restart your terminal after setting the key.

▶️ Usage

Example Python code to test OpenAI API:

from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain Generative AI"
)

print(response.output[0].content[0].text)
🌐 Automation Practice Modules

Used Selenium automation on:

Checkbox Testing

Radio Button Testing

Web Tables Testing

Form Automation

Buttons Interaction

📈 Learning Outcomes

Understanding of Generative AI concepts

AI model integration with Python

Prompt engineering techniques

AI-based web automation

Agentic workflow implementation

🔮 Future Scope

AI Chatbot Integration

AI Test Case Generator

Document Q&A System (RAG)

Voice-enabled AI Assistant

Automated Test Report Generator

🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit pull requests.

📜 License

This project is licensed under the MIT License.
