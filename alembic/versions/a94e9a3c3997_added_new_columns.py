"""added new columns

Revision ID: a94e9a3c3997
Revises: 255d50daaf9e
Create Date: 2025-10-29 01:51:29.723113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a94e9a3c3997'
down_revision: Union[str, Sequence[str], None] = '255d50daaf9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
