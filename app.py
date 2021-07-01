import streamlit as st
import pandas as pd

st.sidebar.header("Texcito Text Reviewer")

st.sidebar.write("### Upload file")
uploaded_file = st.sidebar.file_uploader("Choose a file", type=['csv'])

if uploaded_file:
    st.write(uploaded_file)