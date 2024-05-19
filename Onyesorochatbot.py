import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv
import os
load_dotenv('.env')

API_KEY=os.environ.get("palm_api_key")
palm.configure(api_key=API_KEY)

model= palm.GenerativeModel(model_name="gemini-pro")

st.title("ONYESORO Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages= [
        {
            "role": "assistant", 
            "content": "How can I help you today?"
        }
    ]

for message in st.session_state.messages:
    with st.chat_message( message["role"]) : 
             st.markdown(message["content"])

def llmCall(query):
     response= model.generate_content(query)

     with st.chat_message("assistant"):
          st.markdown(response.text)
        
     st.session_state.messages.append(
        {
           "role": "user",
           "content": query

        }
    )

     st.session_state.messages.append(
        {
           "role": "assistant",
           "content": response.text

        }
    )

query= st.chat_input("Message ONYESORO")
if query: 
     with st.chat_message("user"):
          st.markdown(query)
     llmCall(query= query)

