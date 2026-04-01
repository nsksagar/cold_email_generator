import streamlit as st

st.title('Cold Email generator')
url_input = st.text_input('Enter a URL :', value = "https://jobs.boehringer-ingelheim.com/job/Ridgefield%2C-CT-CMC-Regulatory-Data-Science-Co-Op-%28Hybrid%29-Unit/1368819133/")
submit_button = st.button("Submit")

if submit_button:
    st.code('Hello Hiring Manager, I am from AtliQ', language = 'markdown')



