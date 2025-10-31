"""add forign-key to posts table

Revision ID: a701b49ad46c
Revises: 7bccf82134bd
Create Date: 2025-10-29 23:26:37.955013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a701b49ad46c'
down_revision: Union[str, Sequence[str], None] = '7bccf82134bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",
        local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
pass

def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    
