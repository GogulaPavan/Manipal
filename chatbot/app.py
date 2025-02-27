import streamlit as st
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

# Configure Gemini API
genai.configure(api_key="AIzaSyB_Sfa6qt63_Ap-Qjd86Tavmmg2iiSLgn4")

# Initialize the model
model = genai.GenerativeModel("models/gemini-1.5-pro")

# Function to scrape Manipal Hospital website
def scrape_manipal_info():
    url = "https://www.manipalhospitals.com/vijayawada/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()

# Store website content in cache for quick responses
if "manipal_data" not in st.session_state:
    st.session_state.manipal_data = scrape_manipal_info()

# Streamlit UI with enhanced CSS styles
st.markdown(
    """
    <style>
    /* Main title styling */
    h1 {
        color: #4F8BF9;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 20px;
    }

    /* Subheader styling */
    h2 {
        color: #2E86C1;
        font-size: 1.8rem;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    /* Input field styling */
    .stTextInput input {
        border: 2px solid #4F8BF9;
        border-radius: 5px;
        padding: 10px;
        font-size: 1rem;
    }

    /* Button styling */
    .stButton button {
        background-color: #4F8BF9;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 1rem;
        border: none;
        transition: background-color 0.3s;
    }

    .stButton button:hover {
        background-color: #2E86C1;
    }

    /* Dropdown styling */
    .stSelectbox select {
        border: 2px solid #4F8BF9;
        border-radius: 5px;
        padding: 10px;
        font-size: 1rem;
    }

    /* Response box styling */
    .stMarkdown {
        background-color: #F4F6F6;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #D0D3D4;
        margin-top: 20px;
    }

    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 0.9rem;
        color: #7F8C8D;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Medichat Smart Hospital Management system chatbot")
st.write("Ask me anything about Manipal Hospital Vijayawada!")

# User input
user_query = st.text_input("Your Question:")
if user_query:
    context = st.session_state.manipal_data
    response = model.generate_content(f"{context}\n\nUser Query: {user_query}")
    st.markdown(f"**Chatbot:** {response.text}", unsafe_allow_html=True)
