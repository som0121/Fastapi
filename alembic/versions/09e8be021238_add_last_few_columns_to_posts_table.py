"""add last few columns to posts table

Revision ID: 09e8be021238
Revises: 723fd3702748
Create Date: 2025-10-31 18:21:34.385983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09e8be021238'
down_revision: Union[str, Sequence[str], None] = '723fd3702748'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.column('published'),sa.Boolean(),nullable=False,server_default='TRUE'),
    op.add_column('posts'),sa.column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('Now()')),
   
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
