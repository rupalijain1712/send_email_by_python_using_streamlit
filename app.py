import streamlit as st

import getpass

import smtplib

from mailsend import sendmail

from email.mime.text import MIMEText 

st.header("EMAIL SENDING APP BY RUPALI")

receiver=st.text_input('enter recipient mail id')

sender=st.text_input('enter sender mail id')

pwd=st.text_input('enter password')

subject=st.text_input('enter mail subject')

body=st.text_area('enter mail content')

bu=st.button('CLICK TO SEND MAIL...')

if bu:
    status=sendmail(receiver,sender,pwd,body,subject)
    st.subheader(f" Mail status : {status}")









