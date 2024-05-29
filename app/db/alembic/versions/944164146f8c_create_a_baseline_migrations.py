"""Create a baseline migrations

Revision ID: 944164146f8c
Revises: 
Create Date: 2024-05-29 13:23:53.463621

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '944164146f8c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_queue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipient_address', sa.VARCHAR(length=256), nullable=False),
    sa.Column('email_template_id', sa.VARCHAR(length=256), nullable=False),
    sa.Column('email_template_params', sa.JSON(), nullable=True),
    sa.Column('email_lang', sa.VARCHAR(length=5), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('processed_at', sa.DateTime(), nullable=True),
    sa.Column('processing_result', sa.Integer(), nullable=True),
    sa.Column('processing_error', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('email_attachment_queue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email_queue_id', sa.Integer(), nullable=False),
    sa.Column('email_attachment_path', sa.VARCHAR(length=1024), nullable=True),
    sa.ForeignKeyConstraint(['email_queue_id'], ['email_queue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_email_attachment_queue_email_queue_id'), 'email_attachment_queue', ['email_queue_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_email_attachment_queue_email_queue_id'), table_name='email_attachment_queue')
    op.drop_table('email_attachment_queue')
    op.drop_table('email_queue')
    # ### end Alembic commands ###