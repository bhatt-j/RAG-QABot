# -*- coding: utf-8 -*-
"""Frontend_QABot

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Iw6bPJJ2Mr7iYRNa9keA_tHY2_S-JTn6

# Libraries
"""

import streamlit as st
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer
from backend_qabot import connect_pine, process_pdf, test_queries

"""# Interface"""

st.title("Interactive QA Bot for Financial Data")
st.write("Upload a PDF containing P&L tables and ask financial questions.")

index = connect_pine()

# File uploader
uploaded_file = st.file_uploader("Upload a P&L PDF file", type=["pdf"])

if uploaded_file:
    print("jb-UPLOADED") # for debuging purpose
    if st.button("Process PDF"):
        print("jb-PROCESSING")
        result = process_pdf(uploaded_file, index)
        st.success(result)
        st.write("Data successfully processed and uploaded to Pinecone!")

query = st.text_input("Ask a financial question:")

if query:
  results = test_queries(uploaded_file, query, index)
  # Print the results
  st.write("**Generated Answer:**")
  for match in results["matches"]:
    st.write(f"ID: {match['id']}, Score: {match['score']}, Metadata: {match['metadata']}")