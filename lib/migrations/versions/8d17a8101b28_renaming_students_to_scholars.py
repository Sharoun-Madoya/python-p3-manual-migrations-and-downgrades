"""Renaming students to scholars

Revision ID: 8d17a8101b28
Revises: 791279dd0760
Create Date: 2023-06-01 14:39:48.758334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d17a8101b28'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
