# 🚀 Interview Question Generator

    An advanced RAG (Retrieval-Augmented Generation) powered application that generates high-quality interview questions and answers from any technical document (PDF).

### 📌 Overview

##### Interview Question Generator is a scalable, production-style AI application designed for:

    👨‍💼 Recruiters preparing technical interviews
    👩‍💻 Candidates preparing from documentation
    📚 Anyone wanting structured Q&A from PDFs

###### It leverages Groq Llama 3.1, LangChain, and FAISS to deliver ultra-fast, context-aware results.

### 🛠️ Tech Stack
##### Component	Technology Used
    🧠 LLM	Groq Llama 3.1 8B
    🔗 Orchestration	LangChain (LCEL)
    📊 Vector Database	FAISS
    📐 Embeddings	HuggingFace (all-MiniLM-L6-v2)
    🌐 Backend	Flask
    🎨 Frontend	HTML5 / CSS3 / Vanilla JavaScript
    ⚙️ How to Run Locally
    
### 1️⃣ Create a Conda Environment
```
conda create -p interview python=3.13 -y
```
```
conda activate interview
```
### 2️⃣ Install Requirements
```
pip install -r requirements.txt
```
### 3️⃣ Install the Local Package

This step is crucial for resolving imports from the src/ directory:
```
pip install -e .
```
4️⃣ Setup Environment Variables

### Create a .env file in the root directory and add your Groq API key:
GROQ_API_KEY=your_api_key_here

### 5️⃣ Run the Application
```
python app.py
```
Then open your browser and go to:
```
http://127.0.0.1:8080
```
### 📂 Project Structure
```
Interview_question_generator/
│
├── .github/
│   └── workflows/
│       └── .gitkeep
│
├── data/
│   └── .gitkeep
│
├── artifacts/
│   └── .gitkeep
│
├── vectorstore/
│   └── .gitkeep
│
├── src/
│   └── <project_name>/
│       ├── __init__.py
│       ├── logger.py
│       ├── exception.py
│       │
│       ├── components/
│       │   ├── __init__.py
│       │   ├── data_ingestion.py
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       │   └── model_config.py        # Centralized LLM & Embeddings configuration
│       │
│       ├── pipelines/
│       │   ├── __init__.py
│       │   ├── generation_pipeline.py
│       │   └── rag_pipeline.py
│       │
│       └── utils/
│           ├── __init__.py
│           └── prompts.py             # Prompt templates
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── style.css
│   └── js/
│       └── main.js
│
├── research/
│   └── trials.ipynb                   # Notebook experiments
│
├── app.py
├── requirements.txt
├── setup.py
├── .env
└── README.md
```
### 🧠 Architecture Highlights

    🔹components/ → Core building blocks (data, model, configs)
    🔹pipelines/ → End-to-end workflows (Generation + RAG)
    🔹utils/ → Shared utilities like prompt templates
    🔹vectorstore/ → FAISS index storage
    🔹artifacts/ → Saved models / intermediate outputs
    🔹research/ → Experimental notebooks

#### The project follows a modular, industry-standard architecture ensuring scalability and maintainability.

### 🧠 Project Details & Process Flow
##### 1️⃣ High-Performance Question Generation (Map-Reduce Strategy)

        -> To handle large PDFs efficiently:
             🔹 Map Phase

        -> PDF is split into chunks

        -> Chunks are processed in parallel (multi-threading)

        -> Each chunk generates draft questions using Llama 3.1 on Groq
            🔹 Reduce Phase

        -> Draft questions are aggregated

        -> Duplicates removed

### Final list refined to match user-requested count

    ✔️ Prevents context overflow
    ✔️ Ensures fast response time
    ✔️ Maintains quality control

##### 2️⃣ Intelligent Answering (RAG Pipeline)

        -> Once questions are generated:
            📌 Step 1: Embeddings

        -> Text chunks are converted into numerical vectors using Sentence Transformers.
            📌 Step 2: Vector Search

        -> FAISS performs similarity search to find the most relevant document chunk.
            📌 Step 3: Contextual Answer Generation

        -> The LLM receives:
            📌 The relevant paragraph
            📌 The specific question

        -> This ensures:
            ❌ No hallucinations
            ✅ Context-grounded answers
             High accuracy
            🌐 User Interface
            📄 Upload PDF
            🔢 Select number of questions
            ⚡ Real-time Q&A generation
            💾 Download generated Q&A as text file
            🧹 Clean, responsive Flask-based UI.
            🔥 Key Features
            ⚡ Ultra-fast inference with Groq
            🧠 Map-Reduce parallel processing
            📊 FAISS vector similarity search
            📁 PDF-based contextual understanding
            💡 Scalable modular architecture
            🎯 Hallucination-minimized answers
            📈 Future Improvements
            ⬆️ Add user authentication
            📊 Admin analytics dashboard
            🗂️ Multiple document support
            ☁️ Docker & Cloud deployment

### Contributions are welcome!
### Fork the repository
### Create your feature branch
### Commit your changes
### Open a Pull Request

### 📜 License
    This project is open-source and available under the MIT License.

# ⭐ If You Like This Project
    Give it a ⭐ on GitHub and share it with others!