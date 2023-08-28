"""create address table

Revision ID: 3bb52f4c0f20
Revises: 4d1c52e6ab31
Create Date: 2023-08-27 22:01:01.386577

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3bb52f4c0f20'
down_revision: Union[str, None] = '4d1c52e6ab31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_tavle('address',
                    sa.column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.column('address1',sa.Integer(),nullable=False),
                    sa.column('address2',sa.Integer(),nullable=False),
                    sa.column('city',sa.Integer(),nullable=False),
                    sa.column('state',sa.Integer(),nullable=False),
                    sa.column('country',sa.Integer(),nullable=False),
                    sa.column('postalcode',sa.Integer(),nullable=False),

                    )



def downgrade() -> None:
    op.drop_table('address')
