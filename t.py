import smtplib
from email.message import EmailMessage

# 1. Define configuration and credentials
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # TLS port
SENDER_EMAIL = "jainrupali1712@gmail.com"
APP_PASSWORD = "wvmx ylyq jfok aleo"  # Generated in Step 1
RECIPIENT_EMAIL = "cloudsony999@gmail.com"

# 2. Build the email composition
msg = EmailMessage()
msg["Subject"] = "Automated Test Email"
msg["From"] = SENDER_EMAIL
msg["To"] = RECIPIENT_EMAIL
msg.set_content("Hello! This email was successfully sent from a Python script via Gmail SMTP.")

try:
    # 3. Connect to the Gmail SMTP server
    print("Connecting to server...")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    
    # 4. Upgrade connection to secure TLS mode
    server.starttls()  
    
    # 5. Authenticate and send email
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.send_message(msg)
    
    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email. Error: {e}")

finally:
    # 6. Properly close the session
    server.quit()
