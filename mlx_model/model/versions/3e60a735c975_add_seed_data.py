"""add seed data

Revision ID: 3e60a735c975
Revises: a1a27f27b52
Create Date: 2015-04-20 21:02:57.803350

"""

# revision identifiers, used by Alembic.
revision = '3e60a735c975'
down_revision = 'a1a27f27b52'

from alembic import op
import sqlalchemy as sa


def upgrade():
    group = sa.sql.table(
        'group',
        sa.sql.column('id', sa.Integer),
        sa.sql.column('name', sa.String),
    )

    op.bulk_insert(
        group,
        [
            {'id': 1, 'name': 'administrators'},
            {'id': 2, 'name': 'users'},
            {'id': 3, 'name': 'moderators'},
        ]
    )

    instrument = sa.sql.table(
        'instrument',
        sa.sql.column('id', sa.Integer),
        sa.sql.column('nombre', sa.String),
        sa.sql.column('description', sa.String),
        sa.sql.column('picture', sa.Binary)
    )

    op.bulk_insert(
        instrument,
        [
            {'id': 1, 'nombre': 'Bajo de 4 cuerdas', 'description': 'blah',
             'picture': 'blah'},
            {'id': 2, 'nombre': 'Bajo de 5 cuerdas', 'description': 'blah',
             'picture': 'blah'},
            {'id': 3, 'nombre': 'Bajo de 6 cuerdas', 'description': 'blah',
             'picture': 'blah'},
        ]
    )

    gathering_type = sa.sql.table(
        'gathering_type',
        sa.sql.column('id', sa.Integer),
        sa.sql.column('name', sa.String)
    )

    op.bulk_insert(
        gathering_type,
        [
            {'id': 1, 'name': 'Ensayo'},
            {'id': 2, 'name': 'Ensamble'},
            {'id': 3, 'name': 'Banda'},
            {'id': 4, 'name': 'Concierto'},
        ]
    )


def downgrade():
    pass
