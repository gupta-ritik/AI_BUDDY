import smtplib
from email.mime.text import MIMEText

EMAIL = "ritiknitc@gmail.com"
PASS = "ovid ulyo osgy vrrw"

msg = MIMEText("OTP Test Success")
msg["Subject"] = "SMTP Test"
msg["From"] = EMAIL
msg["To"] = EMAIL

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as s:
    s.login(EMAIL, PASS)
    s.send_message(msg)

print("Email sent successfully")
