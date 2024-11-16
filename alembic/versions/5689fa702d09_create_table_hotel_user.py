"""create table hotel-user

Revision ID: 5689fa702d09
Revises: dd74ffcdb404
Create Date: 2024-11-10 01:40:14.593901

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5689fa702d09'
down_revision: Union[str, None] = 'dd74ffcdb404'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'hotel_user',
        sa.Column('hotel_id', sa.Integer()),
        sa.Column('user_id', sa.Integer())
    )


def downgrade() -> None:
    op.drop_table('hotel_user')