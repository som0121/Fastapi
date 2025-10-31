"""add posts table

Revision ID: 7bccf82134bd
Revises: 84ed2ac6556c
Create Date: 2025-10-29 22:55:51.840624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7bccf82134bd'
down_revision: Union[str, Sequence[str], None] = '84ed2ac6556c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
