import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename 

from src.config import SUBJECT, BODY, ATTACHMENT_PATH
from dotenv import load_dotenv
load_dotenv()

# Sender Info
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")

# Email Info
subject = SUBJECT
body = BODY
attachment_path = ATTACHMENT_PATH

def send_email(receiver_email):
    
    # email setup
    email = MIMEMultipart()
    email['From'] = sender_email
    email['To'] = receiver_email
    email['Subject'] = subject

    email.attach(MIMEText(body, 'plain'))

    with open(attachment_path, "rb") as attachment:
        # Create a MIMEBase object for the attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        
    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {basename(attachment_path)}",
    )

    email.attach(part)

    # Send Email
    with smtplib.SMTP("64.233.184.108", 587) as server:
        server.starttls()
        server.login(sender_email,password)
        server.send_message(email)
        
    print("email send sucessfully.")