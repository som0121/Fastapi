"""add phone_number column to users

Revision ID: d98d63e4e9f3
Revises: a94e9a3c3997
Create Date: 2025-10-29 01:54:17.623311

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd98d63e4e9f3'
down_revision: Union[str, Sequence[str], None] = 'a94e9a3c3997'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
