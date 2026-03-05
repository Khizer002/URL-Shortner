import streamlit as st
import requests

st.title("URL Shortner")
url=st.text_input("Enter your long URL: ")

if st.button("Shorten URL", type="primary"):
    short_url=requests.get(
        f"http://tinyurl.com/api-create.php?url={url}"
    ).text
    st.success("Short URL Generated")
    st.code(short_url)