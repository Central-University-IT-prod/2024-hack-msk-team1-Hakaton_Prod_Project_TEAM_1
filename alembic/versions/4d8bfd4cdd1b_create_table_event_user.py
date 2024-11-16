"""create table event_user

Revision ID: 4d8bfd4cdd1b
Revises: f7c5db9a9fc1
Create Date: 2024-11-08 20:43:18.964222

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4d8bfd4cdd1b'
down_revision: Union[str, None] = 'f7c5db9a9fc1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'event_user',
        sa.Column('event_id', sa.Integer()),
        sa.Column('user_id', sa.Integer())
    )


def downgrade() -> None:
    op.drop_table('event_user')
