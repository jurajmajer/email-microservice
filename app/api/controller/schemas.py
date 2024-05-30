from typing import List

from pydantic import BaseModel


class EmailAttachment(BaseModel):
    filename: str
    filepath: str


class SendEmailItem(BaseModel):
    recipientAddress: str
    subject: str
    templateId: str
    templateParams: object | None = None
    lang: str | None = 'en'
    attachments: List[EmailAttachment] | None = None
