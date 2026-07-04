from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv(".env")


# set the title of the app

st.set_page_config(page_title="LangChain Google Generative AI", page_icon=":robot_face:")

# Define the function to generate response from the model

def model_generate(text):
    llm_model = ChatGoogleGenerativeAI(google_api_key=os.getenv("GOOGLE_API_KEY"), temperature=0.6, model="gemini-2.5-flash")
    response=llm_model.invoke(text)
    return response.text

# input text from the user

# set the background color of the app

st.markdown("""
<style>
body {
  background: #ff0099; 
  background: -webkit-linear-gradient(to right, #ff0099, #493240); 
  background: linear-gradient(to right, #ff0099, #493240); 
}
</style>
    """, unsafe_allow_html=True)

user_input = st.text_area("Enter your text here:", height=50)

if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        response = model_generate(user_input)
        st.write(response)
if len(user_input) == 0:
    st.warning("Please enter some text to generate a response.")