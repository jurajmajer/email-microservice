from typing import List

from pydantic import BaseModel


class SendEmailItem(BaseModel):
    recipientAddress: str
    subject: str
    templateId: str
    templateParams: object | None = None
    lang: str | None = 'en'
    attachments: List[str] | None = None
