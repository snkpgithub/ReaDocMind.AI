# 📘 ReaDocMind.AI
🚀 **An AI-powered research assistant that helps you analyze and search through PDFs using advanced language models.**

---

## 🌟 Features
✔ **Upload PDFs** and extract meaningful insights  
✔ **AI-powered Q&A** – Ask questions and get answers from the document  
✔ **Fast and local processing** (No cloud dependencies, runs free on your machine!)  
✔ **Uses Large Language Models (LLMs)** for intelligent responses  
✔ **Embeddings-based search** for retrieving relevant information  

---

## 🛠️ Tech Stack
- **Python** 🐍  
- **Streamlit** (for UI)  
- **LangChain** (for document processing)  
- **Ollama LLM** (for local AI responses)  
- **Vector Database (InMemory)** (for fast retrieval)  
- **PDFPlumber** (for document parsing)  
- **DeepSeek LLM** (for document understanding and question answering)  

---

## 🔍 How **DeepSeek** Works in ReadMind.AI
**DeepSeek LLM** is an advanced AI model that powers document understanding and question-answering in ReadMind.AI. Here's how it works:

1. **PDF Processing**: The document text is extracted using **PDFPlumber**.
2. **Text Chunking & Embeddings**: The extracted text is broken into smaller chunks and converted into vector representations using **DeepSeek embeddings**.
3. **Vector Search**: When a user asks a question, the app searches for relevant document chunks using similarity search.
4. **AI-Powered Answering**: The retrieved context is fed into **DeepSeek LLM**, which generates concise and factual responses.
5. **Interactive UI**: The processed information is displayed in a conversational chat interface for easy readability.

DeepSeek enhances **accuracy, relevance, and AI reasoning**, making ReadMind.AI a **powerful research assistant**.  

---

## 🚀 Installation Guide
### 1️⃣ Clone this repository
```sh
git clone https://github.com/snkpgithub/ReaDocMind.AI.git
cd ReaDocMind.AI
```

### 2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the application
```sh
streamlit run rag_deep.py
```
Then open **http://localhost:8501** in your browser.

---

## 📂 Folder Structure
```
📁 ReaDocMind.AI/
│── 📂 src/                    # Source code
│    │── 📄 rag_deep.py        # Main AI-powered Streamlit app
│── 📂 document_store/         # Stores uploaded PDFs (optional)
│── 📂 models/                 # LLM model configs (if needed)
│── 📂 requirements.txt        # Dependencies list
│── 📂 README.md               # Project documentation
│── 📂 LICENSE                 # (Optional) License file
```

---

## 🛠️ Future Improvements
🔹 **Multi-PDF support** – Analyze multiple documents at once  
🔹 **Persistent database** – Store and retrieve previously indexed documents  
🔹 **Deploy on Streamlit Cloud** – Make it accessible online  
🔹 **Better UI** – Interactive design improvements  

---

## 🤝 Contributing
If you’d like to contribute:
1. Fork the repository 🍴  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Make your changes and commit (`git commit -m "Added new feature"`)  
4. Push to GitHub (`git push origin feature-branch`)  
5. Open a pull request!  

---

## 📜 License
This project is licensed under the **MIT License** – free to use and modify.

---

## 📩 Contact
🔹 **Created by:** Shashank Pandey  
🔹 **GitHub:** [snkpgithub](https://github.com/snkpgithub)  
🔹 **Email:** (Add your email if comfortable)  

---

### 🎯 If you like this project, don't forget to ⭐ the repo! 🌟  
