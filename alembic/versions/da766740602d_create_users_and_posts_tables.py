"""create users and posts tables

Revision ID: da766740602d
Revises: d221195e8e53
Create Date: 2025-10-09 10:26:43.874932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da766740602d'
down_revision: Union[str, Sequence[str], None] = 'd221195e8e53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(255), nullable=False, unique=True),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('phone_number', sa.String(20), nullable=True),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )

    # Posts table
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('content', sa.Text, nullable=False),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('published', sa.Boolean, server_default='true', nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )

    # Votes table (many-to-many)
    op.create_table(
        'votes',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True),
        sa.Column('post_id', sa.Integer, sa.ForeignKey('posts.id', ondelete='CASCADE'), primary_key=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('votes')
    op.drop_table('posts')
    op.drop_table('users')



