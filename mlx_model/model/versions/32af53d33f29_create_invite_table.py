"""create invite table

Revision ID: 32af53d33f29
Revises: 1cf307da902c
Create Date: 2015-04-20 16:53:42.848901

"""

# revision identifiers, used by Alembic.
revision = '32af53d33f29'
down_revision = '1cf307da902c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'invite',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('gathering_id', sa.Integer, sa.ForeignKey('gathering.id')),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id'))
    )


def downgrade():
    op.drop_table(
        'invite'
    )
