"""empty message

Revision ID: 3fadeaea1474
Revises: dcb93f425c70
Create Date: 2020-01-21 14:57:28.476962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fadeaea1474'
down_revision = 'dcb93f425c70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entry', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'entry', 'user', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'entry', type_='foreignkey')
    op.drop_column('entry', 'author_id')
    # ### end Alembic commands ###
