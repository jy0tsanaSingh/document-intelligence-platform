import streamlit as st
import requests

BASE_URL = "http://localhost:8000/documents"

st.title("📄 Document Intelligence Platform")

filename = st.text_input("Document Filename")

if st.button("Upload Document"):
    response = requests.post(
        BASE_URL,
        json={"filename": filename},
    )

    if response.status_code == 200:
        st.success("Document uploaded successfully!")
        document = response.json()
        st.session_state["document_id"] = document["id"]
        st.json(document)
    else:
        st.error("Upload failed")


if "document_id" in st.session_state:
    if st.button("Process Document"):
        response = requests.post(
            f"{BASE_URL}/{st.session_state['document_id']}/process"
        )

        if response.status_code == 200:
            st.success("Document processed!")
            st.json(response.json())
        else:
            st.error("Processing failed")
