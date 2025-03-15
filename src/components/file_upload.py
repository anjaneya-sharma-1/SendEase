import streamlit as st
import pandas as pd

def upload_file():
    uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            if 'Name' in df.columns and 'Email' in df.columns:
                st.success("File uploaded successfully!")
                return df
            else:
                st.error("The uploaded file must contain 'Name' and 'Email' columns.")
                return None
        except Exception as e:
            st.error(f"Error reading the file: {e}")
            return None
    return None