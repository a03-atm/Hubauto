import streamlit as st

st.set_page_config(page_title="Hub Auto", page_icon="🚗", layout="wide")

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=1000, scrolling=True)
