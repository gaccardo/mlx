"""add state_id to invite

Revision ID: 24963cf04232
Revises: 3e60a735c975
Create Date: 2015-04-20 21:21:32.670933

"""

# revision identifiers, used by Alembic.
revision = '24963cf04232'
down_revision = '3e60a735c975'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column(
        'invite',
        sa.Column('state_id', sa.Integer,
                  sa.ForeignKey('invitation_states.id'))
    )


def downgrade():
    op.drop_column(
        'invite',
        'state_id'
    )
