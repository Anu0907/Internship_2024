from openai import OpenAI
import streamlit as st

# Read the API key and Setup an OpenAI Client
f = open('keys/.openAI_API_key.txt')
key = f.read()
client = OpenAI(api_key = key)

st.title("An AI Code Reviewer")

# If the button is clicked, generate responses
def code_review(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are a helpful AI Assistant. Take python code as an input from the user.
            Give the bugs explaination and generate a fixed code snippet as an output.\n`python\n{code}\n`python"""},
            {"role": "user", "content": f"fix and explain the bugs in the python code {prompt}"}
        ]
    )
    return response.choices[0].message.content

# Take User's input
code = st.text_area("Enter a Python Code here...", height=150)

# Button to submit code for review
if st.button("Review"):
    st.header("Code Review")
    feedback = code_review(code)
    st.write(feedback)