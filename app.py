from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os
from openai import OpenAI



load_dotenv()  #take the env variables from dotenv

## function to load openai model and get response

def get_openai_response(question):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        stream=True,
    )

    response = ""

    for chunk in stream:
        response += chunk.choices[0].delta.content or ""

    return response

##initialize our streamlit
    
st.set_page_config(page_title="Q&A App")
st.header("ConvoCraft")

input = st.text_input("Let's chat! Type away and share your thoughts", key="input")
response = get_openai_response(input)

submit = st.button("Generate")

## if ask is clicked

if submit:
    st.subheader("You're in for a treat! Here's your response...")
    st.write(response)