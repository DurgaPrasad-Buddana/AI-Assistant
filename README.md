<img width="1129" height="547" alt="Image1" src="https://github.com/user-attachments/assets/f631daa0-b65d-4935-b915-8f5a918e4dfd" />

<div align="center">

# 🤖⚡ AI Document Q&A Chatbot

### Chat with your PDFs using the power of Generative AI!

*Upload any document. Ask anything. Get instant, accurate, context-aware answers.*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6F00?style=for-the-badge)

</div>

---

## 🌟 What is this project?

Ever wished you could just **talk to your documents** instead of scrolling through 50 pages looking for one answer? That's exactly what this project does.

This is an **AI-powered RAG (Retrieval-Augmented Generation) chatbot** that lets you upload any PDF and instantly start a conversation with it. Under the hood, it combines the reasoning power of **OpenAI's GPT models** with a **semantic vector search engine**, so answers come straight from *your* document — not a hallucinated guess. 

Built completely from scratch as a hands-on deep dive into how real-world Generative AI applications are built — from raw PDF text all the way to a live, memory-aware chatbot. 🚀

---

## 🎯 Why I built this

I wanted to go beyond "just calling an LLM API" and actually understand the **full RAG pipeline** — chunking strategy, embeddings, vector similarity search, prompt engineering, and conversational memory — the exact architecture powering real production AI assistants today. 

---

## ✨ Key Features

| Feature | Description |
|---|---|
|  **PDF Upload & Parsing** | Drop in any PDF and it's automatically parsed and indexed |
|  **Conversational Memory** | Remembers the last 5 exchanges, so follow-up questions just work |
|  **Semantic Search** | Finds the *most relevant* chunks of your document, not just keyword matches |
|  **Real-Time Answers** | Ask a question, get a grounded answer in seconds |
|  **Auto Re-Indexing** | Upload a new file and the bot instantly forgets the old one and learns the new one |
|  **Clean Text Pipeline** | Strips encoding noise from extracted PDF text for cleaner embeddings |

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
|  **Frontend / UI** | Streamlit |
|  **Orchestration** | LangChain |
|  **LLM (Brain)** | OpenAI GPT |
|  **Embeddings** | OpenAI Embeddings |
|  **Vector Database** | ChromaDB |
|  **Document Parsing** | PyPDF |

</div>

---

## 🏗️ How It Works — The Architecture

```mermaid
flowchart TD
    A[📄 User uploads PDF] --> B[🔍 PyPDFLoader parses document]
    B --> C[✂️ Text Splitter<br/>chunk_size=1000, overlap=150]
    C --> D[🧹 Clean chunk text]
    D --> E[📐 OpenAI Embeddings]
    E --> F[(🗄️ Chroma Vector Store)]
    G[💬 User asks a question] --> H[🔎 Retriever: top-3 similarity search]
    F --> H
    H --> I[🧠 Conversational Retrieval Chain]
    J[🧠 Memory: last 5 turns] --> I
    I --> K[🤖 OpenAI GPT generates answer]
    K --> L[✅ Answer shown in Streamlit UI]
    L --> J
```

**Process in simple steps:** Your PDF gets sliced into bite-sized chunks → each chunk becomes a vector (a mathematical representation of its meaning) → when you ask a question, the app finds the *most relevant* chunks → feeds them + your chat history to GPT → GPT crafts a grounded, accurate answer. ✨

---

## 📸 Screenshots

| Upload Screen |
*<img width="1129" height="547" alt="Image1" src="https://github.com/user-attachments/assets/947bdecd-7d36-4cbf-aea0-d65a9cf7b6a4" />* 

| Chat in Action |
*<img width="1172" height="617" alt="image2" src="https://github.com/user-attachments/assets/a97135d5-b0f0-4d85-bcaf-3a8add288535" />*  
*<img width="1269" height="678" alt="image3" src="https://github.com/user-attachments/assets/1369f43f-199d-4b04-a674-ecb37f570e3d" />* 
*<img width="1320" height="832" alt="image4" src="https://github.com/user-attachments/assets/4f55d23f-3347-433c-b6ac-ee768dda5e68" />* 

---

## 🚀 Getting Started

### 1️⃣ Clone the repo
```bash
git clone https://github.com/DurgaPrasad-Buddana/AI-Assistant.git
cd <your-repo-name>
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add your OpenAI API key
```bash
cp .env.example .env
# then open .env and paste your key:
# OPENAI_API_KEY=sk-...
```

### 5️⃣ Run it! 🎉
```bash
streamlit run app.py
```

Open `http://localhost`, upload a PDF, and start chatting with your document! 💬

Note: due to API constraints unable to provide localhost.
---

## 📊 Performance Snapshot

| Metric | Result |
|---|---|
|  Avg. response time | ~2–4 seconds per query |
|  Indexing time | ~5–10 seconds for a 20-page PDF |
|  Manual QA accuracy | ~85–90% on test document sets |
|  Memory window | Last 5 conversational turns |

*(Metrics based on local testing — not large-scale benchmarking.)*

---

## 🧠 What I Learned

Building this project pushed me to understand:
-  How **RAG pipelines** actually work end-to-end, not just in theory
-  Why **chunking strategy** and **overlap size** massively impact answer quality
-  How to design **conversational memory** so a chatbot feels genuinely context-aware
-  How **prompt engineering** shapes whether an LLM stays grounded or starts hallucinating
-  How to structure a Streamlit app with proper session state management

---

## 🔮 Future Enhancements 

- [ ] Support for multiple file formats (DOCX, TXT, CSV)
- [ ] Multi-document knowledge base support
- [ ] Token-by-token streaming responses
- [ ] Swap to a production-grade vector DB (Pinecone/Weaviate)
- [ ] Automated evaluation suite (e.g. RAGAS) for accuracy tracking

---

## 🙌 Connect With Me

If you found this project interesting, feel free to ⭐ star the repo or connect with me!

<div align="center">

**Built with 💙 and a lot of curiosity about Generative AI**

</div>
