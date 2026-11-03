"""auto-vote

Revision ID: e3767024c0b5
Revises: 09e8be021238
Create Date: 2025-10-31 20:14:03.075886

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3767024c0b5'
down_revision: Union[str, Sequence[str], None] = '09e8be021238'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Superseded by 84ed2ac6556c, which creates the full schema.
    pass


def downgrade() -> None:
    pass
