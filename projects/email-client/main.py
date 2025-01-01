import smtplib, ssl
from email.mime.text import MIMEText

port = 465  # For SSL

# Ask for credentials
sender_email = input("Enter your email: ")
password = input("Enter your password: ")

# Create a secure SSL context
context = ssl.create_default_context()

# gmail domain to handle requests
smtp_server = "smtp.gmail.com"

# Create smtp object with SSL protections
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    
    # Login
    server.login(sender_email, password)

    # TODO: Send email here
    
    text = """\
    Hello!!! with 3 exclamation points!
    """

    # Create MIMEText object
    message = MIMEText(text, "plain")
    message["Subject"] = "Plain text email"
    message["From"] = sender_email
    message["To"] = sender_email

    # Send email to oneself
    server.sendmail(sender_email, sender_email, message.as_string())

    print('Sent')
