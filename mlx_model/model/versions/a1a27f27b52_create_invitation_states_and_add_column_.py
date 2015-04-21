"""create invitation_states and add column state to invite table

Revision ID: a1a27f27b52
Revises: 32af53d33f29
Create Date: 2015-04-20 20:45:27.422651

"""

# revision identifiers, used by Alembic.
revision = 'a1a27f27b52'
down_revision = '32af53d33f29'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'invitation_states',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )

    invitation_states = sa.sql.table(
        'invitation_states',
        sa.sql.column('id', sa.Integer),
        sa.sql.column('name', sa.String)
    )

    op.bulk_insert(invitation_states,
        [
            {'name': 'Accepted', 'id': 1},
            {'name': 'Canceled', 'id': 2},
            {'name': 'Waiting',  'id': 3}
        ]
    )

    #op.add_column(
    #    'invite',
    #    sa.Column('state_id', sa.Integer,
    #              sa.ForeignKey('invitation_states.id'))
    #)


def downgrade():
    op.drop_table('invitation_states')
    #op.drop_column('invite', 'state_id')
