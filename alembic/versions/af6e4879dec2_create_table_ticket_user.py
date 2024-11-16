"""create table ticket-user

Revision ID: af6e4879dec2
Revises: 5689fa702d09
Create Date: 2024-11-10 01:42:00.462707

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af6e4879dec2'
down_revision: Union[str, None] = '5689fa702d09'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ticket-user',
        sa.Column('ticket_id', sa.Integer()),
        sa.Column('user_id', sa.Integer())
    )


def downgrade() -> None:
    op.drop_table('ticket-user')
