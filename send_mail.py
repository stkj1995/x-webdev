from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_verify_email(user_email, user_verification_key):
    try:
        sender_email = "sophieteinvigkjer@gmail.com"
        app_password = "ukqveyvvlsrhinwd"  # Use App Password from Google

        # Create the email
        message = MIMEMultipart()
        message["From"] = "My company name"
        message["To"] = user_email
        message["Subject"] = "Please verify your account"

        body = f"""
        <h1 style="font-family: avenir, sans-serif">Verify your account</h1> 
        <p>Click the link below to verify your account:</p>
        <a href="http://127.0.0.1:5000/verify/{user_verification_key}">Verify Account</a>
        """
        message.attach(MIMEText(body, "html"))

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, user_email, message.as_string())

        print("Verification email sent!")
        return True

    except Exception as e:
        print("Error sending email:", e)
        return False
