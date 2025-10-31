"""add foreign-key to posts table

Revision ID: 723fd3702748
Revises: a701b49ad46c
Create Date: 2025-10-31 17:59:40.860188

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '723fd3702748'
down_revision: Union[str, Sequence[str], None] = 'a701b49ad46c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
