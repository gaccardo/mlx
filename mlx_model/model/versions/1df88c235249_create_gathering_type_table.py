"""create gathering_type table

Revision ID: 1df88c235249
Revises: 1c5e11023e72
Create Date: 2015-04-20 14:42:12.781033

"""

# revision identifiers, used by Alembic.
revision = '1df88c235249'
down_revision = '1c5e11023e72'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'gathering_type',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )


def downgrade():
    op.drop_table('gathering_type')
