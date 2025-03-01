import streamlit as st
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# --- Modern Dark Theme ---
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: #FFFFFF;
    }
    
    .stSidebar {
        background-color: #1A1A1A !important;
        padding: 20px;
        border-radius: 10px;
    }
    
    .stChatInput input {
        background-color: #2C2C2C !important;
        color: #FFFFFF !important;
        border: 1px solid #444444 !important;
        border-radius: 10px;
        padding: 12px;
    }
    
    .stChatMessage[data-testid="stChatMessage"] {
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
    }
    
    .stChatMessage[data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #1E1E1E !important;
        color: #E0E0E0 !important;
    }
    
    .stChatMessage[data-testid="stChatMessage"]:nth-child(even) {
        background-color: #262626 !important;
        color: #F0F0F0 !important;
    }
    
    .stFileUploader {
        background-color: #1E1E1E;
        border: 1px solid #444;
        border-radius: 8px;
        padding: 15px;
    }
    
    h1, h2, h3 {
        text-align: center;
        color: #00FFAA !important;
    }
    
    .footer {
        text-align: center;
        font-size: 14px;
        padding: 15px;
        color: #AAAAAA;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Constants ---
PROMPT_TEMPLATE = """
You are an expert research assistant. Use the provided context to answer the query. 
If unsure, state that you don't know. Be concise and factual (max 3 sentences).

Query: {user_query} 
Context: {document_context} 
Answer:
"""

#PDF_STORAGE_PATH = 'document_store/pdfs/'
EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")
DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")

# --- Functions ---
"""def save_uploaded_file(uploaded_file):
    file_path = PDF_STORAGE_PATH + uploaded_file.name
    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())
    return file_path"""
import tempfile

def save_uploaded_file(uploaded_file):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.getbuffer())  # Write file contents
        return temp_file.name  # Return the temporary file path

def load_pdf_documents(file_path):
    document_loader = PDFPlumberLoader(file_path)
    return document_loader.load()

def chunk_documents(raw_documents):
    text_processor = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    return text_processor.split_documents(raw_documents)

def index_documents(document_chunks):
    DOCUMENT_VECTOR_DB.add_documents(document_chunks)

def find_related_documents(query):
    return DOCUMENT_VECTOR_DB.similarity_search(query)

def generate_answer(user_query, context_documents):
    context_text = "\n\n".join([doc.page_content for doc in context_documents])
    conversation_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    response_chain = conversation_prompt | LANGUAGE_MODEL
    return response_chain.invoke({"user_query": user_query, "document_context": context_text})

# --- UI Configuration ---
st.title("📘 ReaDocMind.AI")
st.markdown("## Document analysis for your research needs.")
st.markdown("### Upload your PDF document and ask questions to get answers from the content.")
st.markdown("---")

# Sidebar for File Upload
with st.sidebar:
    st.header("📂 Upload Your PDF")
    uploaded_pdf = st.file_uploader(
        "Upload Research Document",
        type="pdf",
        help="Select a PDF document for analysis",
        accept_multiple_files=False
    )

if uploaded_pdf:
    saved_path = save_uploaded_file(uploaded_pdf)
    raw_docs = load_pdf_documents(saved_path)
    processed_chunks = chunk_documents(raw_docs)
    index_documents(processed_chunks)
    
    st.success("✅ Document processed successfully! Ask your questions below.")
    
    user_input = st.chat_input("Enter your question about the document...")
    
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        
        with st.spinner("Analyzing document..."):
            relevant_docs = find_related_documents(user_input)
            ai_response = generate_answer(user_input, relevant_docs)
            
        with st.chat_message("assistant", avatar="🤖"):
            st.write(ai_response)

# --- Footer ---
st.markdown("<div class='footer'>Created by <b>Shashank Pandey</b></div>", unsafe_allow_html=True)
