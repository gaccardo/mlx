"""add is_public to gathering table

Revision ID: 3c795c70a5e8
Revises: 240637e39d69
Create Date: 2015-04-20 14:57:59.955410

"""

# revision identifiers, used by Alembic.
revision = '3c795c70a5e8'
down_revision = '240637e39d69'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'gathering',
        sa.Column('is_public', sa.Boolean))


def downgrade():
    op.drop_column(
        'gathering',
        'is_public')
