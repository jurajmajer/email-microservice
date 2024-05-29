from sqlalchemy import Column, Integer, VARCHAR, JSON, ForeignKey, DateTime, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TEXT

Base = declarative_base()
metadata = Base.metadata


class EmailQueue(Base):
    __tablename__ = 'email_queue'

    id = Column(Integer, primary_key=True)
    recipient_address = Column(VARCHAR(256), nullable=False)
    email_template_id = Column(VARCHAR(256), nullable=False)
    email_template_params = Column(JSON)
    email_lang = Column(VARCHAR(5))
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    processed_at = Column(DateTime)
    processing_result = Column(Integer)
    processing_error = Column(TEXT)


class EmailAttachmentQueue(Base):
    __tablename__ = 'email_attachment_queue'

    id = Column(Integer, primary_key=True)
    email_queue_id = Column(ForeignKey('email_queue.id'), nullable=False, index=True)
    email_attachment_path = Column(VARCHAR(1024))
