import pandas as pd

def read_excel_file(file_path):
   
    try:
        df = pd.read_excel(file_path)
        if 'Email' not in df.columns:
            raise ValueError("Excel file must contain 'Email' column.")
        return df
    except Exception as e:
        raise ValueError(f"Error reading the Excel file: {e}")

def validate_email(email):
   
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def extract_names_and_emails(df):
 
    valid_entries = []
    for _, row in df.iterrows():
        email = row['Email']
        if validate_email(email):
 
            recipient_data = row.to_dict()
            valid_entries.append(recipient_data)
        else:
            print(f"Invalid email format: {email}")
    return valid_entries