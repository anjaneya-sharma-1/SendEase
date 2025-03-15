import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.config.settings import SMTP_SERVER, SMTP_PORT

def send_email(sender_email, sender_password, to_email, subject, body):
    
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls() 
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        return True
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")
        return False

def send_bulk_emails(sender_email, sender_password, recipients_data, email_subject, email_template):
    
    success_count = 0
    failed_count = 0
    failed_emails = []
    
    for recipient in recipients_data:
        try:
         
            personalized_body = email_template.format(**recipient)
            email = recipient['Email']
            
            if send_email(sender_email, sender_password, email, email_subject, personalized_body):
                success_count += 1
            else:
                failed_count += 1
                failed_emails.append(email)
        except KeyError as e:
            print(f"Missing placeholder key in template: {e}")
            failed_count += 1
            failed_emails.append(recipient.get('Email', 'Unknown'))
    
    return success_count, failed_count, failed_emails