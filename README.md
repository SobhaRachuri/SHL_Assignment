# SHL_Assignment
SHL Assessment Recommendation System 

# 🧠 SHL Assessment Recommendation Engine

This project is a **Web-based Retrieval-Augmented Generation (RAG)** tool built using **Streamlit**, designed to recommend SHL assessments based on natural language job descriptions or queries.

---

## 🚀 Demo

🌐 [Live Web App] https://shlassignment-a9eizpcefsh3w42ppdkqrj.streamlit.app/  
📂 [GitHub Repository] https://github.com/SobhaRachuri

---

## 🧰 Features

- 📝 Accepts natural language queries (e.g., JD or skill requirements).
- ⚙️ Uses embedding-based retrieval with cosine similarity.
- 📊 Evaluation metrics like **Mean Recall@3** and **MAP@3** implemented.
- 🧠 Optionally integrates LLMs (e.g., OpenAI, Gemini) to enhance relevance.
- 🖼️ Clean UI using **Streamlit**.

---

## 🔧 How It Works

1. User enters a query (e.g., JD or skills).
2. Query is encoded using embedding models.
3. Relevant SHL assessments are retrieved based on semantic similarity.
4. Optional: LLM summarizes the match rationale.
5. Evaluation done using benchmark queries and metrics.

---

## 📂 Folder Structure
📁 SHL_Assignment/ ├── app.py # Main Streamlit app ├── evaluate.py # Evaluation metrics script (Recall@3, MAP@3) ├── data/ │ └── assessments.csv # SHL catalog or embedding data ├── utils/ │ └── rag_utils.py # Embedding, similarity, and helper functions ├── README.md # Project overview

## 🧪 Evaluation Metrics

The solution has been tested using a benchmark set, and the following results were achieved:

- 🎯 **Mean Recall@3**: `1.0`
- 📊 **MAP@3**: `1.0`

These high scores indicate the system's strong ability to retrieve relevant assessments accurately for given job descriptions.



