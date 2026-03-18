import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyDLS9crwogs47DR6AkIOeSN5C3gqINk97w")
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("Talk to Agent")
st.write("This app demonstrates how to use Google Gemini API with Streamlit")

user_input = st.text_input("Ask Anything:")
if st.button("Submit"):
    with st.spinner("Generating response..."):
        response = model.generate_content(user_input)
    st.write(response.text)