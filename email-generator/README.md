# 📩 Cold Email Generator using LLMs

Generate personalized, human-like cold emails automatically from job postings using **Large Language Models (LLMs)**.

This project extracts job details from a given URL and generates a concise, professional cold email tailored to the opportunity.

---

# 🚀 Live Demo

🔗 https://cold-email-generator-bibisifhat.streamlit.app/

---

# 🧠 How It Works

1. User pastes a **job posting URL**
2. The app **scrapes the webpage content**
3. Extracts **structured job data using an LLM**
4. Matches **relevant skills from your project database**
5. Generates a **personalized cold email**
6. Allows **download of the generated email**

---

# 🛠 Tech Stack

- **Streamlit** – Web interface  
- **LangChain** – LLM orchestration  
- **Groq (LLaMA 3.3 70B)** – Language model  
- **ChromaDB** – Vector similarity search  
- **Pandas** – CSV data handling  
- **BeautifulSoup** – Web scraping  

---

# 🔐 Environment Setup

Create a `.env` file in the root directory:
