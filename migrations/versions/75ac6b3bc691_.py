"""empty message

Revision ID: 75ac6b3bc691
Revises: f316c79fa193
Create Date: 2017-02-22 23:01:01.251200

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '75ac6b3bc691'
down_revision = 'f316c79fa193'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hosts', sa.Column('callDuration', sa.Integer(), nullable=True))
    op.add_column('hosts', sa.Column('dayEnd', sa.DateTime(), nullable=True))
    op.add_column('hosts', sa.Column('dayStart', sa.DateTime(), nullable=True))
    op.add_column('sales_rep', sa.Column('avgLeadCallConversion', sa.FLOAT(), nullable=True))
    op.add_column('sales_rep', sa.Column('avgResponseTime', sa.FLOAT(), nullable=True))
    op.add_column('sales_rep', sa.Column('totalCallsScheduled', sa.Integer(), nullable=True))
    op.add_column('sales_rep', sa.Column('totalEmailsReceived', sa.Integer(), nullable=True))
    op.add_column('sales_rep', sa.Column('totalEmailsReviewedByHomans', sa.Integer(), nullable=True))
    op.add_column('sales_rep', sa.Column('totalEmailsSent', sa.Integer(), nullable=True))
    op.drop_column('sales_rep', 'authenticated')
    op.drop_column('sales_rep', 'hostName')
    op.drop_column('sales_rep', 'callDuration')
    op.drop_column('sales_rep', 'active')
    op.drop_column('sales_rep', 'dayEnd')
    op.drop_column('sales_rep', 'dayStart')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales_rep', sa.Column('dayStart', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('sales_rep', sa.Column('dayEnd', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('sales_rep', sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('sales_rep', sa.Column('callDuration', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('sales_rep', sa.Column('hostName', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('sales_rep', sa.Column('authenticated', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('sales_rep', 'totalEmailsSent')
    op.drop_column('sales_rep', 'totalEmailsReviewedByHomans')
    op.drop_column('sales_rep', 'totalEmailsReceived')
    op.drop_column('sales_rep', 'totalCallsScheduled')
    op.drop_column('sales_rep', 'avgResponseTime')
    op.drop_column('sales_rep', 'avgLeadCallConversion')
    op.drop_column('hosts', 'dayStart')
    op.drop_column('hosts', 'dayEnd')
    op.drop_column('hosts', 'callDuration')
    # ### end Alembic commands ###
