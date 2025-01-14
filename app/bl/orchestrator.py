import logging
from datetime import datetime

import app.bl.email.smtp_email_sender as email_sender
from app.bl.email import email_composer
from app.db.models import EmailQueue

log = logging.getLogger(__name__)


def orchestrate(db):
    emails_to_process = db.query(EmailQueue).filter(EmailQueue.processed_at.is_(None)).all()
    for email in emails_to_process:
        process_email(email, db)


def process_email(email, db):
    try:
        email_content_pathes = email_composer.compose_email(email.template_id,
                                                            email.template_params, email.lang)
        email_sender.send_email(email.recipient_address,
                                email.subject, email_content_pathes, email.attachments)
    except Exception as e:
        email.processing_result = 1
        email.processing_error = repr(e)
        log.exception(e)
    else:
        email.processing_result = 0
    finally:
        email.processed_at = datetime.now()
        db.commit()
