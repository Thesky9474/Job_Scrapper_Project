import smtplib
import ssl
import re
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config_loader import get_config

config = get_config()
sender_email = config["SENDER_EMAIL"]
receiver_email = config["RECEIVER_EMAIL"]
password = config["EMAIL_PASSWORD"]

df = pd.read_csv("internshala_jobs.csv")
df["Parsed Stipend"] = df["Stipend"].apply(
    lambda x: int(re.findall(r"\d+", x.replace(",", ""))[0]) if isinstance(x, str) and re.search(r"\d+", x) else 0)
new_jobs = df[df["Parsed Stipend"] > 0].head(5)

body = "<h3>🔥 Top Internship Picks:</h3><ul>"
for _, row in new_jobs.iterrows():
    body += f"<li><b>{row['Title']}</b> at {row['Company']} – {row['Location']} | Stipend: {row['Stipend']}</li>"
body += "</ul>"

msg = MIMEMultipart()
msg["Subject"] = "🔔 Internship Alert (Top Picks)"
msg["From"] = sender_email
msg["To"] = receiver_email
msg.attach(MIMEText(body, "html"))

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("✅ Email sent!")