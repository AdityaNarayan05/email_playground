import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Aditya Narayan Jaiswal'
email['to'] = 'adityanarayanjaiswal05@gmail.com'
email['subject'] = 'You won 1,000,000 rupee!'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('nadityajaiswal05@gmail.com', 'Aditya@1')
    smtp.send_message(email)
    print('all good boss!')
