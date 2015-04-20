"""add is_valid column to token table

Revision ID: 580f39689260
Revises: 2b8751087ecc
Create Date: 2015-04-20 09:04:21.689724

"""

# revision identifiers, used by Alembic.
revision = '580f39689260'
down_revision = '2b8751087ecc'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'token',
        sa.Column('is_valid', sa.Boolean))


def downgrade():
    op.drop_column(
        'token',
        'is_valid')
