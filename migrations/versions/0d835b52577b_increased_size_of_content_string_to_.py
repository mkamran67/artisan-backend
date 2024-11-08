"""Increased size of content string, to better handle larger answers.

Revision ID: 0d835b52577b
Revises: 864297718de4
Create Date: 2024-11-07 21:15:57.261658

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d835b52577b'
down_revision: Union[str, None] = '864297718de4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('messages', 'content',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=5000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('messages', 'content',
               existing_type=sa.String(length=5000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
    # ### end Alembic commands ###