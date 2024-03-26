import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from getpass import getpass

def send_email():
    SMTP_HOST = "smtp.gmail.com"
    SMTP_PORT = 587
    FROM_ADDRESS = 'your_email@gmail.com'

    try:
        password = getpass("Enter your password: ")
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.ehlo()
        server.starttls()
        server.login(FROM_ADDRESS, password)
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Please check your email and password.")
        return
    except smtplib.SMTPException as e:
        print("An error occurred while connecting to the email server:", str(e))
        return

    TO_ADDRESS = 'target_email@...'
    SUBJECT = 'Subject'
    CONTENT = """
    Content
    """

    msg = MIMEMultipart()
    msg['From'] = FROM_ADDRESS
    msg['To'] = TO_ADDRESS
    msg['Subject'] = SUBJECT
    body = MIMEText(CONTENT, 'html')
    msg.attach(body)

    FILE_PATH = r"path"
    FILE_NAME = 'file.txt'
    try:
        with open(FILE_PATH, 'rb') as attachment:
            att = MIMEBase('application', 'octet-stream')
            att.set_payload(attachment.read())
            encoders.encode_base64(att)
            att.add_header('Content-Disposition', f'attachment; filename="{FILE_NAME}"')
            msg.attach(att)
    except IOError:
        print("Failed to attach the file. Please check the file path.")
        server.quit()
        return

    try:
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Email sent!")
    except smtplib.SMTPException as e:
        print("An error occurred while sending the email:", str(e))
    finally:
        server.quit()

send_email()
