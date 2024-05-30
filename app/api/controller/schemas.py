from typing import List

from pydantic import BaseModel


class SendMessageItem(BaseModel):
    recipientAddress: str
    templateId: str
    templateParams: object | None = None
    lang: str | None = 'en'
    attachments: List[str] | None = None
