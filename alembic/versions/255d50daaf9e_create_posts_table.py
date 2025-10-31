"""create posts table

Revision ID: 255d50daaf9e
Revises: 
Create Date: 2025-10-28 23:38:37.924479

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '255d50daaf9e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('title', sa.String(), primary_key=True,nullable=False),
        sa.Column('posts',sa.String(),primary_key=True,nullable=False)
    )


def downgrade() -> None:
    op.drop_table('posts')
