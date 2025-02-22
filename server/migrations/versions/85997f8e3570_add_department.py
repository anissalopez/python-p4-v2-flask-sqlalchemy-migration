"""add department

Revision ID: 85997f8e3570
Revises: f3939bff61a5
Create Date: 2023-11-11 10:46:47.263343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85997f8e3570'
down_revision = 'f3939bff61a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
