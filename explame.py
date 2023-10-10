import smtplib


import os
from email.mime.text import MIMEText

def send_text(message):
    sender = 'artykovh@gmail.com'
    to_send = 'artykovh2@gmail.com'
    gmail = 'kwvh tnih tpia kvrl'
    password2 = 'kwvh tnih tpia kvrl'
    
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    try:
        server.login(sender,password2)
        msg = MIMEText(message)
        msg['Subject'] = 'Click me'
        server.sendmail(sender,to_send, msg.as_string())
        
        return 'message was send'
    except Exception as _ex:
        return f'{_ex} check login or pass'
    
    
def main():
    message = input('TYpe message: ')
    print(send_text(message=message))
    
    
if __name__ == '__main__':
    main()
    
    
    


