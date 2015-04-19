"""create user_group table

Revision ID: 3f0895f2edf2
Revises: 2680f7972125
Create Date: 2015-04-19 20:39:17.576322

"""

# revision identifiers, used by Alembic.
revision = '3f0895f2edf2'
down_revision = '2680f7972125'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user_group',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')),
        sa.Column('group_id', sa.Integer, sa.ForeignKey('group.id'))
    )


def downgrade():
    op.drop_table('user_group')
