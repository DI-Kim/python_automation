import smtplib
import os
# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

GMAIL_ID = os.getenv('GMAIL_ID')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')

conn = smtplib.SMTP('smtp.gmail.com', 587)
print(conn)

print(conn.ehlo())
print(conn.starttls())

conn.login(GMAIL_ID, GMAIL_PASSWORD)


## 보내는 이메일, 받는 이메일, 내용(Subject는 제목, \n\n을 사용하여 본문으로 넘어감)
conn.sendmail('weaponofjungle@gmail.com', 'daein7076@naver.com', 'Subject: So long...\n\nDear bigPerson, thanks for all the fish\n-Daein')

print(conn.quit())