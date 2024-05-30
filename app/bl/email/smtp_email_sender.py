import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.bl import util

sender_address = util.read_env_var('SENDER_ADDRESS')
username = util.read_env_var('SMTP_USERNAME')
password = util.read_env_var('SMTP_PASSWORD')
smtp_server = util.read_env_var('SMTP_SERVER')
smtp_port = util.read_env_var('SMTP_PORT', False, 465)


def send_email(recipient_address, subject, html_content_path, attachments):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_address
    message["To"] = recipient_address

    with open(html_content_path, encoding='utf-8') as f:
        html_content = f.read()
        if html_content is None:
            raise Exception('Cannot send email: html_content is null')
        message.attach(MIMEText(html_content, "html", _charset='utf-8'))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(username, password)
        server.sendmail(
            sender_address, recipient_address, message.as_string()
        )
