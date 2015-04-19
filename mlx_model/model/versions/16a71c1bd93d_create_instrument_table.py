"""create instrument table

Revision ID: 16a71c1bd93d
Revises: None
Create Date: 2015-04-19 18:47:22.507368

"""

# revision identifiers, used by Alembic.
revision = '16a71c1bd93d'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'instrument',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        sa.Column('picture', sa.Binary),
    )


def downgrade():
    op.drop_table('instrument')
