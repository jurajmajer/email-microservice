import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.bl import util

sender_address = util.read_env_var('SENDER_ADDRESS')
username = util.read_env_var('SMTP_USERNAME')
password = util.read_env_var('SMTP_PASSWORD')
smtp_server = util.read_env_var('SMTP_SERVER')
smtp_port = util.read_env_var('SMTP_PORT', False, 465)
attachment_root = util.read_env_var('ATTACHMENT_ROOT', False)


def send_email(recipient_address, subject, email_content_pathes, attachments):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_address
    message["To"] = recipient_address

    if email_content_pathes[0] is not None:
        with open(email_content_pathes[0], encoding='utf-8') as f:
            plain_content = f.read()
            message.attach(MIMEText(plain_content, "plain", _charset='utf-8'))

    if email_content_pathes[1] is not None:
        with open(email_content_pathes[1], encoding='utf-8') as f:
            html_content = f.read()
            message.attach(MIMEText(html_content, "html", _charset='utf-8'))

    if attachments is not None:
        for attachment in attachments:
            message = handle_attachment(message, attachment)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        server.login(username, password)
        server.sendmail(
            sender_address, recipient_address, message.as_string()
        )


def handle_attachment(message, attachment):
    if attachment_root is None:
        raise Exception('Cannot send email with attachments because '
                        'environment variable ATTACHMENT_ROOT is not set')
    with open(os.path.join(attachment_root, attachment.filepath), "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment.filename}",
    )
    message.attach(part)
    return message
