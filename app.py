# Brian Lesko
# 4/20/2024
# This script sends an email using the smtplib library

import smtplib
from email.message import EmailMessage
from secrets import SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL


msg = EmailMessage()
msg.set_content(
    """
    Hello, this is an encrypted, simple email sent from Python!
    """)


msg['Subject'] = 'An Automated Email'
msg['To'] = RECIPIENT_EMAIL

server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # use SSL for security
#server.starttls() # use TLS (Transport Layer Security)
server.login(SENDER_EMAIL, SENDER_PASSWORD)
server.send_message(msg)
server.quit()


