"""create user_instrument table

Revision ID: 1c5e11023e72
Revises: 580f39689260
Create Date: 2015-04-20 14:02:21.045527

"""

# revision identifiers, used by Alembic.
revision = '1c5e11023e72'
down_revision = '580f39689260'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user_instrument',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('instrument_id', sa.Integer, sa.ForeignKey('instrument.id'))
    )


def downgrade():
    op.drop_table('user_instrument')
