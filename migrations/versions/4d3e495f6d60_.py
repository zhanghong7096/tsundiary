"""empty message

Revision ID: 4d3e495f6d60
Revises: 126c3a2178f6
Create Date: 2014-10-28 08:58:12.648445

"""

# revision identifiers, used by Alembic.
revision = '4d3e495f6d60'
down_revision = '126c3a2178f6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('timezone', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'timezone')
    ### end Alembic commands ###
