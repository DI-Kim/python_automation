import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

GMAIL_ID = os.getenv('GMAIL_ID')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')

conn = smtplib.SMTP('smtp.gmail.com', 587)
print(conn)

print(conn.ehlo())
print(conn.starttls())

conn.login(GMAIL_ID, GMAIL_PASSWORD)

conn.sendmail('weaponofjungle@gmail.com', 'daein7076@naver.com', 'Subject: So long...\n\nDear bigPerson, thanks for all the fish\n\n-Daein')

print(conn.quit())