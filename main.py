from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure Google API with the provided API key
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Initialize the Google Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get a response from Google Gemini
def get_gemini_response(content, prompt):
    response = model.generate_content([content, prompt])
    return response.text

# Function to handle the chat
def handle_chat(user_message):
    # Fixed prompt for generating a response
    prompt = f"""
    You are a helpful chatbot providing financial advice. Based on the user's message, provide accurate and helpful financial information or advice.
    User's Message: {user_message}
    """
    
    # Get response from Gemini
    response = get_gemini_response(user_message, prompt)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Financial Chatbot", layout="wide")
st.title("Financial Chatbot")

# Chat input
user_message = st.text_input("Enter your message")

if st.button("Get Response"):
    if user_message:
        response = handle_chat(user_message)
        st.subheader("Chatbot Response")
        st.write(response)
    else:
        st.error("Please enter a message.")
