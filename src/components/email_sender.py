import streamlit as st
from src.utils.email_utils import send_bulk_emails
from src.utils.excel_utils import extract_names_and_emails

def send_emails(sender_email, sender_password, df, email_subject, email_body):
   
    with st.spinner("Sending emails..."):
        recipients = extract_names_and_emails(df)
        
        if not recipients:
            st.error("No valid email addresses found in the file.")
            return 0, 0, []
        
      
        if len(recipients) > 0:
            try:
                first_recipient = recipients[0]
                preview = email_body.format(**first_recipient)
                with st.expander("Preview of first email"):
                    st.text(preview)
            except KeyError as e:
                st.warning(f"Preview failed - missing column: {e}")
        
        success, failed, failed_emails = send_bulk_emails(
            sender_email, 
            sender_password, 
            recipients, 
            email_subject, 
            email_body
        )
        
        return success, failed, failed_emails