import streamlit as st
import os
import pandas as pd
import sys
import re
from pathlib import Path


root_path = str(Path(__file__).parent.parent)
if root_path not in sys.path:
    sys.path.append(root_path)

from src.components.file_upload import upload_file
from src.components.email_form import email_form
from src.components.email_sender import send_emails


st.set_page_config(page_title="Email Sender App", page_icon="✉️")

def main():
    st.title("Bulk Email Sender")
    st.write("Send personalized emails to multiple recipients using an Excel file")
    
  
    tab1, tab2, tab3 = st.tabs(["1. Credentials", "2. Upload Excel", "3. Email Content"])
    

    with tab1:
        st.header("Email Credentials")
        st.warning("⚠️ Credentials are stored locally in your session and not sent anywhere.")
        
        if 'sender_email' not in st.session_state:
            st.session_state.sender_email = ""
        if 'sender_password' not in st.session_state:
            st.session_state.sender_password = ""
        
        sender_email = st.text_input("Your Gmail Address", 
                                   value=st.session_state.sender_email,
                                   placeholder="your.email@gmail.com")
        sender_password = st.text_input("Your Gmail App Password", 
                                      type="password", 
                                      value=st.session_state.sender_password,
                                      placeholder="16-character app password",
                                      help="Use an App Password, not your regular password. Create one at: https://myaccount.google.com/apppasswords")
        
        if st.button("Save Credentials"):
            st.session_state.sender_email = sender_email
            st.session_state.sender_password = sender_password
            st.success("✅ Credentials saved to session!")
    
    
    with tab2:
        df = upload_file()
        if df is not None:
            st.session_state.df = df
            st.write("Preview of your data:")
            st.dataframe(df.head())
            
            st.success(f"Found {len(df.columns)} columns: {', '.join(df.columns.tolist())}")
            st.info("You can use any column name as a placeholder in your email by typing {ColumnName}")
    
   
    with tab3:
        available_columns = None
        if 'df' in st.session_state:
            available_columns = st.session_state.df.columns.tolist()
        
        email_subject, email_body = email_form(available_columns)
     
        if 'df' in st.session_state:
            placeholders = re.findall(r'\{([^}]+)\}', email_body)
            invalid_placeholders = [p for p in placeholders if p not in st.session_state.df.columns]
            if invalid_placeholders:
                st.warning(f"⚠️ These placeholders were not found in your data: {', '.join(invalid_placeholders)}")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("Send Emails", type="primary"):
                if 'sender_email' not in st.session_state or not st.session_state.sender_email:
                    st.error("❌ Please enter your Gmail address first")
                elif 'sender_password' not in st.session_state or not st.session_state.sender_password:
                    st.error("❌ Please enter your Gmail app password first")
                elif 'df' not in st.session_state:
                    st.error("❌ Please upload an Excel file first")
                else:
                    success, failed, failed_emails = send_emails(
                        st.session_state.sender_email,
                        st.session_state.sender_password,
                        st.session_state.df,
                        email_subject,
                        email_body
                    )
                    
                    if success > 0:
                        st.success(f"✅ Successfully sent {success} emails")
                    
                    if failed > 0:
                        st.error(f"❌ Failed to send {failed} emails")
                        st.error("Failed emails: " + ", ".join(failed_emails))

if __name__ == "__main__":
    main()