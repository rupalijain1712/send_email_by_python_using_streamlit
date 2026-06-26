# Email Sending App — Python + Streamlit + SMTP

A lightweight web app for sending emails straight from a browser — no email client required. Built with **Streamlit** for the UI and Python's built-in **smtplib** to deliver mail through Gmail's SMTP server.

> Pure Python &nbsp;|&nbsp; Single-Page UI &nbsp;|&nbsp; TLS-Encrypted SMTP &nbsp;|&nbsp; Zero Database / Backend

---

## Features

- **One-page form** to compose and send an email — recipient, sender, subject, and body in a single view
- **Direct Gmail SMTP delivery** using `smtplib` with `STARTTLS` encryption — no third-party mail API needed
- **Instant feedback** — the send status is displayed back in the UI immediately after the button click
- **Minimal footprint** — just two small Python files, no database or external service required

---

## Project Structure

| File / Folder | Purpose |
|---|---|
| **`app.py`** | Streamlit front-end — renders the input form and triggers the send action |
| **`mailsend.py`** | Core mail logic — builds the MIME message and handles the SMTP handshake |

---

## How It Works

```
User fills in recipient, sender, password, subject, and body
        ↓
Clicks "CLICK TO SEND MAIL..."
        ↓
app.py calls mailsend.sendmail(receiver, sender, pwd, body, subject)
        ↓
mailsend.py wraps the body in a MIMEText object
        ↓
Connects to smtp.gmail.com → upgrades to TLS via starttls()
        ↓
Authenticates and sends the message through Gmail's SMTP server
        ↓
A status string is returned and shown back in the Streamlit UI
```

---

## App Inputs

| Field | Widget | Purpose |
|---|---|---|
| Recipient mail ID | `st.text_input` | Email address the message will be sent to |
| Sender mail ID | `st.text_input` | Email address used to authenticate and send |
| Password | `st.text_input` | Gmail App Password used for SMTP login |
| Subject | `st.text_input` | Subject line of the email |
| Content | `st.text_area` | Body text of the email |
| Click to send mail | `st.button` | Triggers `sendmail()` and displays the result |

---

## Functions Reference

| Function | File | Purpose |
|---|---|---|
| `sendmail(receiver, sender, pwd, body, subject)` | `mailsend.py` | Builds a `MIMEText` email, connects to Gmail's SMTP server over TLS, authenticates, and sends the message |

---

## Getting Started

**Requirements:**
- Python 3.10 or later
- A Gmail account with [2-Step Verification](https://myaccount.google.com/security) enabled and an **App Password** generated (Gmail SMTP rejects your regular account password)
- `streamlit` installed (`smtplib` and `email` are part of the Python standard library — no install needed)

**Local Setup:**

```bash
# 1. Clone the repository
git clone https://github.com/rupalijain1712/send_email_by_python_using_streamlit.git

# 2. Navigate to the project folder
cd send_email_by_python_using_streamlit

# 3. Install dependencies
pip install streamlit

# 4. Run the app
streamlit run app.py
```

Streamlit will open the app automatically in your browser at `http://localhost:8501`.

---

## Security Notes

- **Never commit real credentials.** Use a Gmail **App Password**, not your main account password, and keep it out of source control.
- **Mask the password field** by passing `type="password"` to `st.text_input()` so it isn't shown in plain text on screen.
- For repeated/local use, consider storing default credentials in [`st.secrets`](https://docs.streamlit.io/develop/concepts/connections/secrets-management) or environment variables instead of typing them in each run.

---

## Future Improvements

- Mask the password input field on the UI
- Add CC/BCC and file attachment support
- Validate email address format before sending
- Move default credentials to `st.secrets` / environment variables
- Friendlier error handling for failed logins or network issues
- Support additional providers (Outlook, Yahoo) via a dropdown
- Add a `requirements.txt` for reproducible installs

---

## Tech Stack

| Technology | Role | Why Chosen |
|---|---|---|
| **Python 3** | Core language | Simple syntax, built-in email/SMTP support |
| **Streamlit** | Web UI | Turns a plain Python script into a web app with no HTML/CSS/JS |
| **smtplib** | SMTP client | Standard library — no extra dependency for sending mail |
| **email.mime.text** | Message construction | Builds a properly formatted MIME email object |
| **Gmail SMTP** | Mail delivery | Free, reliable, widely supported via `smtp.gmail.com` |

---

## Use Cases

- Quick utility for sending one-off emails without opening a mail client
- Educational project for learning SMTP + Streamlit integration
- Starter template for building a custom mailer or notification tool
- Portfolio project demonstrating Python email automation

---

## Developer

Rupali Jain
