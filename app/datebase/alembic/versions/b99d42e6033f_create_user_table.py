"""create user table

Revision ID: b99d42e6033f
Revises: 350bbb0c0038
Create Date: 2024-12-12 23:46:05.854578

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b99d42e6033f'
down_revision: Union[str, None] = '350bbb0c0038'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
