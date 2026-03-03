🚀 SHL RAG Assessment Recommender

A Retrieval-Augmented Generation (RAG) based intelligent recommendation system that suggests the most relevant SHL assessments based on hiring queries or job descriptions.

Built as part of the SHL technical assignment.

🧠 Overview

This system uses semantic search and vector similarity to recommend suitable SHL assessments for a given hiring requirement.

It leverages transformer embeddings and FAISS indexing for efficient retrieval.

⚙️ Tech Stack

Python

Sentence Transformers (all-MiniLM-L6-v2)

FAISS (Vector Similarity Search)

Gradio (Web Interface)

Pandas

🏗️ How It Works

SHL assessment catalogue is processed and stored.

Embeddings are generated using Sentence Transformers.

Embeddings are indexed using FAISS.

A user query is converted into an embedding.

Top-K similar assessments are retrieved.

Recommendations are returned in structured format.

📂 Repository Structure
shl-rag-assignment/
│
├── app.py                 # Gradio web application
├── rag_engine.py          # Core retrieval engine
├── requirements.txt       # Dependencies
├── models/                # FAISS index and metadata
└── README.md
🚀 Run Locally
1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
2️⃣ Run the Web App
python app.py
🧪 Generate Predictions (Batch Mode)

If using batch prediction script:

python generate_predictions.py

Output file:

yashwanth_varakuti.csv
📌 Example Output
Query,predictions
Hire Java Developer,Java 8 (New) | Core Java (Advanced Level) | Global Skills Assessment
🎯 Key Features

Semantic similarity search

Efficient vector indexing with FAISS

Clean recommendation output

Deployable via Hugging Face Spaces

👨‍💻 Author

Yashwanth Varakuti

GitHub: https://github.com/Yashwanthvarakuti
