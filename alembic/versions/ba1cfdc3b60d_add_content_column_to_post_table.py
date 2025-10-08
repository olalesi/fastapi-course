"""add content column to post table

Revision ID: ba1cfdc3b60d
Revises: c161f1acfca4
Create Date: 2025-10-08 09:27:14.630616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba1cfdc3b60d'
down_revision: Union[str, Sequence[str], None] = 'c161f1acfca4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    """Downgrade schema."""
    pass
