"""empty message

Revision ID: 74ca6623beaa
Revises: ec03e6777c26
Create Date: 2017-02-20 18:11:24.553157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74ca6623beaa'
down_revision = 'ec03e6777c26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales_rep', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('sales_rep', sa.Column('authenticated', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sales_rep', 'authenticated')
    op.drop_column('sales_rep', 'active')
    # ### end Alembic commands ###
