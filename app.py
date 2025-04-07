import streamlit as st
import pandas as pd
from google.generativeai import configure, GenerativeModel

# Load SHL catalog
catalog_df = pd.read_csv("shl_assessment_catalog.csv")

# Gemini API Configuration
configure(
    api_key="AIzaSyBKvLhrgGqzCod7gMbxwK2fbdJ0JuflAXo",
    transport="rest"
)

# Gemini Model
model = GenerativeModel(
    model_name="models/gemini-1.5-pro-latest",
    generation_config={"temperature": 0.7}
)

# Generate recommendation prompt
def get_recommendations(query, df, top_k=10):
    context = "\n".join([
        f"{row['Assessment Name']} - {row['Test Type']} - {row['Duration']} - Remote: {row['Remote Testing Support']} - Adaptive: {row['Adaptive/IRT Support']}"
        for _, row in df.iterrows()
    ])

    prompt = f"""
    Based on the following assessment catalog:

    {context}

    Recommend up to {top_k} relevant SHL assessments for the following query:
    "{query}"

    Return a table with these columns:
    Assessment Name, Assessment URL, Remote Testing Support, Adaptive/IRT Support, Duration, Test Type
    """
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")

# 💄 Custom Styling for MAX Appeal
st.markdown("""
    <style>
        body, .main {
            background: linear-gradient(135deg, #74ebd5 0%, #9face6 100%);
            font-family: 'Segoe UI', sans-serif;
            color: #1e272e;
        }

        .title {
            text-align: center;
            font-size: 44px;
            font-weight: 900;
            color: #000000;
            text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
            margin-bottom: 0.5rem;
        }

        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #ffcocb;
            margin-bottom: 2rem;
        }

        .box {
            background: rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 35px;
            border-radius: 20px;
            box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.1);
            max-width: 900px;
            margin: auto;
            margin-top: 20px;
        }

        .stTextArea > div > textarea {
            font-size: 16px !important;
            background-color: #ffffffdd;
            border-radius: 10px;
        }

        .footer {
            margin-top: 50px;
            text-align: center;
            font-size: 15px;
            color: blue;
        }

        .stButton>button {
            background: #2c3e50;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 10px;
            font-weight: bold;
            font-size: 16px;
            transition: 0.3s;
        }

        .stButton>button:hover {
            background: #1abc9c;
            color: black;
            transform: scale(1.03);
        }
    </style>
""", unsafe_allow_html=True)

# Page Title & Subtitle
# Title with SHL Logo on the left
# SHL Logo + Title using st.image and layout
# Title + Logo inline with no gap using HTML
col1, col2 = st.columns([2, 4])
with col1:
    st.image("shl_logo.png", width=100)
with col2:
    st.markdown("""
        <div style="font-size: 38px; font-weight: 900; color: #000000; text-shadow: 2px 2px 6px rgba(0,0,0,0.2); margin-top: 10px;">
            SHL Assessment Recommendation Engine
        </div>
    """, unsafe_allow_html=True)

# Subtitle
st.markdown('<div class="subtitle">🚀 Get customized SHL assessment suggestions for your dream candidates!</div>', unsafe_allow_html=True)

# Input & Results Container
st.markdown('<div class="box">', unsafe_allow_html=True)
query = st.text_area("💼 Enter job description or hiring query:", height=150, placeholder="e.g., Hiring Java developers with strong business communication...")

if st.button("✨ Get Smart Recommendations"):
    if query.strip():
        with st.spinner("⏳ Generating your custom SHL assessment plan..."):
            result = get_recommendations(query, catalog_df)
            st.markdown(result, unsafe_allow_html=True)
    else:
        st.warning("Please enter a query to proceed.")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">⚡Elementary Model Designed by Sobha Rachuri 👩‍💻✨Built With Passion, Powered By Intelligence ✨</div>', unsafe_allow_html=True)
