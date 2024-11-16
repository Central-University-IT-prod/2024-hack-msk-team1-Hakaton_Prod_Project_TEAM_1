"""create table hotel

Revision ID: dd74ffcdb404
Revises: b956da834031
Create Date: 2024-11-10 01:35:09.673072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd74ffcdb404'
down_revision: Union[str, None] = 'b956da834031'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'hotel',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('hotel')
