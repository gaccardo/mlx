"""create group table

Revision ID: 2680f7972125
Revises: 19f0ba5ed905
Create Date: 2015-04-19 20:35:38.014754

"""

# revision identifiers, used by Alembic.
revision = '2680f7972125'
down_revision = '19f0ba5ed905'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'group',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('group')
