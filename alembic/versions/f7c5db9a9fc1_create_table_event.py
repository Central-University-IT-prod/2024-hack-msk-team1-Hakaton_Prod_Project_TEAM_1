"""create table event

Revision ID: f7c5db9a9fc1
Revises: aeff4f544603
Create Date: 2024-11-08 20:39:01.825028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f7c5db9a9fc1'
down_revision: Union[str, None] = 'aeff4f544603'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'event',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('spending', sa.Integer(), nullable=False),
        sa.Column('date', sa.String(), nullable=False),
        sa.Column('reason', sa.String(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('event')
