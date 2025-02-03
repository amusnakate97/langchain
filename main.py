### Integrate code with OpenAI

import openai
from constants import OPEN_AI_API_KEY  # Fixed typo in import statement
import os
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"] = OPEN_AI_API_KEY

st.title("LangChain Demo with OpenAI")
input_text = st.text_input("Search a topic")

llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))