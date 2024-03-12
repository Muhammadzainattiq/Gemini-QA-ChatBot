from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question)
    return response.text


st.set_page_config(page_title = "Gemini Q&A")
st.markdown("""
    <style>
        .header {
            font-size: 36px;
            color: #1E90FF; /* Change the color as per your preference */
            text-align: center;
            margin-bottom: 30px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2); /* Add shadow effect */
        }
            .response {
            font-size: 24px;
            color: green; /* Change the color as per your preference */
            text-align: left;
            margin-bottom: 20px;
        }
           
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="header">Gemini ChatBot with History</h1>', unsafe_allow_html=True)


if 'chat_history' not in st.session_state:
    st.session_state["chat_history"] = []

input = st.text_input("Input: ", key = "input")
submit = st.button("Ask the Question")

if submit and input:
    response = get_gemini_response(input)

    ##Add user query and response to session chat history
    st.session_state["chat_history"].append({"question": input, "answer": response})
    st.subheader("Response: ")
    for message in reversed(st.session_state["chat_history"]):
        st.write(f"**You:** {message['question']}")
        st.write(f"**Gemini:** {message['answer']}")
        st.write("---")

