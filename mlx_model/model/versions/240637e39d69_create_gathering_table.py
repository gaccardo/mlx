"""create gathering table

Revision ID: 240637e39d69
Revises: 1df88c235249
Create Date: 2015-04-20 14:54:06.878623

"""

# revision identifiers, used by Alembic.
revision = '240637e39d69'
down_revision = '1df88c235249'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'gathering',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('gathering_type_id', sa.Integer,
                  sa.ForeignKey('gathering_type.id')),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('user.id'))
    )


def downgrade():
    op.drop_table('gathering')
