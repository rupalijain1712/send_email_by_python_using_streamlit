import getpass

import smtplib

from email.mime.text import MIMEText 

def sendmail(receiver,sender,pwd,body,subject):

    m=MIMEText(body)

    m['From']=receiver
    m['To']=sender
    m['Subject']=subject

    server=smtplib.SMTP("smtp.gmail.com",)

    server.starttls()

    server.login(receiver,pwd)

    server.send_message(m)

    server.quit()

    return 'MAIL SEND ... CHECK MAILBOX NOW!!!!'



# print(sendmail("cloudsony999@gmail.com","jainrupali1712@gmail.com","wvmx ylyq jfok aleo","hi ..","test"))




