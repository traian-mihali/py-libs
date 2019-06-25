from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(Path('template.html').read_text())
body = template.substitute({"name": "John Doe"})

message = MIMEMultipart()
message["from"] = "sender's name"
message["to"] = "recipient"
message["subject"] = "Test"
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("logo.jpg").read_bytes()))

try:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("email_address", "password")
        smtp.send_message(message)
        print("email sent...")
except Exception as ex:
    print(ex)
