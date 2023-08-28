"""create phone number for user col

Revision ID: 1a6d3ba014e7
Revises: 
Create Date: 2023-08-27 21:51:34.427792

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a6d3ba014e7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('user',sa.Column('phoe_nmber',sa.Integer(),nullable=True))



def downgrade() -> None:
    op.drop_column('users','phone_number')
