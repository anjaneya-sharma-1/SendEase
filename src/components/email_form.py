import streamlit as st

def email_form(available_columns=None):
    st.header("Email Content Form")
    
    if available_columns:
        placeholder_examples = ", ".join([f"{{{col}}}" for col in available_columns[:5]])
        if len(available_columns) > 5:
            placeholder_examples += ", ..."
        st.info(f"Available placeholders: {placeholder_examples}")
    
    email_subject = st.text_input("Email Subject", "Your Subject Here")
    default_body = "Hello {Name},\n\nThis is your message.\n\nBest Regards,\nYour Name"
    email_body = st.text_area("Email Body", default_body, height=200)

    return email_subject, email_body