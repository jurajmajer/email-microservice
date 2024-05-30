from app.api.controller.schemas import SendEmailItem
from app.db.database import SessionLocal
from app.db.models import EmailQueue, EmailAttachmentQueue


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def schedule_email(body: SendEmailItem, db):
    email_queue = EmailQueue()
    email_queue.recipient_address = body.recipientAddress
    email_queue.subject = body.subject
    email_queue.template_id = body.templateId
    email_queue.template_params = body.templateParams
    email_queue.lang = body.lang
    if body.attachments is not None:
        for attachment in body.attachments:
            item = EmailAttachmentQueue()
            item.attachment_path = attachment
            email_queue.attachments.append(item)
    db.add(email_queue)
    db.commit()
