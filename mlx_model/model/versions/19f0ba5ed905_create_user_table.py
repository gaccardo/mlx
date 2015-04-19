"""create user table

Revision ID: 19f0ba5ed905
Revises: 16a71c1bd93d
Create Date: 2015-04-19 20:01:48.695857

"""

# revision identifiers, used by Alembic.
revision = '19f0ba5ed905'
down_revision = '16a71c1bd93d'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils.types as st


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('firstname', sa.String(50), nullable=False),
        sa.Column('lastname', sa.String(50), nullable=False),
        sa.Column('email', sa.String(150), nullable=False),
        sa.Column('picture', sa.Binary, nullable=True),
        sa.Column('password', st.password.PasswordType(
            schemes=['md5_crypt'],
        )))


def downgrade():
    op.drop_table('user')
