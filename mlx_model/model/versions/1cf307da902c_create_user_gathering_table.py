"""create user_gathering table

Revision ID: 1cf307da902c
Revises: 3c795c70a5e8
Create Date: 2015-04-20 15:03:19.895655

"""

# revision identifiers, used by Alembic.
revision = '1cf307da902c'
down_revision = '3c795c70a5e8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user_gathering',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('participant_id', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('gathering_id', sa.Integer, sa.ForeignKey('gathering.id')))

def downgrade():
    op.drop_table('user_gathering')
