"""create token table

Revision ID: 2b8751087ecc
Revises: 3f0895f2edf2
Create Date: 2015-04-19 20:50:24.791688

"""

# revision identifiers, used by Alembic.
revision = '2b8751087ecc'
down_revision = '3f0895f2edf2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'token',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('token', sa.String(50), nullable=False),
        sa.Column('datetime', sa.DateTime(), server_default="now()",
                  nullable=False),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('user.id')))


def downgrade():
    op.drop_table('token')
