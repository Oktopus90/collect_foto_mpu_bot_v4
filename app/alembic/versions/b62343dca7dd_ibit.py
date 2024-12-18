"""ibit

Revision ID: b62343dca7dd
Revises: 
Create Date: 2024-12-18 15:42:28.454175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b62343dca7dd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('telegram_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('edited_at', sa.DateTime(), nullable=True),
    sa.Column('unique_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('unique_id'),
    sa.UniqueConstraint('telegram_id'),
    sa.UniqueConstraint('username'),
    )
    op.create_table('kontrolpoints',
    sa.Column('number', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('adres', sa.String(length=255), nullable=True),
    sa.Column('district', sa.String(length=255), nullable=True),
    sa.Column('question', sa.String(length=255), nullable=True),
    sa.Column('discription', sa.String(length=255), nullable=True),
    sa.Column('comments', sa.String(length=255), nullable=True),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('author_id', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('edited_at', sa.DateTime(), nullable=True),
    sa.Column('unique_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.unique_id'] ),
    sa.PrimaryKeyConstraint('unique_id'),
    sa.UniqueConstraint('number'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kontrolpoints')
    op.drop_table('users')
    # ### end Alembic commands ###
