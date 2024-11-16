"""create table ticket

Revision ID: b956da834031
Revises: 4d8bfd4cdd1b
Create Date: 2024-11-08 20:47:40.486973

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b956da834031'
down_revision: Union[str, None] = '4d8bfd4cdd1b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'ticket',
        sa.Column('id', sa.String(), nullable=False, autoincrement=True),
        sa.Column('race_number', sa.String()),
        sa.Column('date_arrive', sa.String()),
        sa.Column('date_comeback', sa.String()),
        sa.Column('price', sa.Integer),
        sa.Column('Home', sa.String()),
        sa.Column('away', sa.String())
    )


def downgrade() -> None:
    op.drop_table('ticket')
