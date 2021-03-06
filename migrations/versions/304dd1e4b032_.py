"""empty message

Revision ID: 304dd1e4b032
Revises: 52eba4f06ee0
Create Date: 2017-02-28 20:41:57.679351

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '304dd1e4b032'
down_revision = '52eba4f06ee0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lead_threads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('salesRep', sa.String(length=120), nullable=True),
    sa.Column('threadId', sa.String(length=120), nullable=True),
    sa.Column('subject', sa.TEXT(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('firstName', sa.String(length=120), nullable=True),
    sa.Column('company', sa.String(length=120), nullable=True),
    sa.Column('status', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('callTime', sa.DateTime(), nullable=True),
    sa.Column('interest', sa.Integer(), nullable=True),
    sa.Column('review', sa.Boolean(), nullable=True),
    sa.Column('reviewReason', sa.TEXT(), nullable=True),
    sa.Column('msgIds', sa.TEXT(), nullable=True),
    sa.Column('latestReply', sa.TEXT(), nullable=True),
    sa.Column('latestParticipants', sa.TEXT(), nullable=True),
    sa.Column('conversationText', sa.TEXT(), nullable=True),
    sa.Column('sentEmailCount', sa.Integer(), nullable=True),
    sa.Column('receivedEmailCount', sa.Integer(), nullable=True),
    sa.Column('lastEmailSentTime', sa.DateTime(), nullable=True),
    sa.Column('lastEmailReceivedTime', sa.DateTime(), nullable=True),
    sa.Column('frontConversationId', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['salesRep'], ['sales_rep.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('leads')
    op.add_column('gCredentials', sa.Column('credType', sa.String(length=120), nullable=True))
    op.add_column('hosts', sa.Column('salesRepName', sa.String(length=120), nullable=True))
    op.add_column('hosts', sa.Column('salesRepSignature', sa.TEXT(), nullable=True))
    op.drop_column('hosts', 'assistantName')
    op.drop_column('hosts', 'assistantSignature')
    op.add_column('sales_rep', sa.Column('totalLeadsManaged', sa.Integer(), nullable=True))
    op.drop_column('sales_rep', 'avgLeadCallConversion')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales_rep', sa.Column('avgLeadCallConversion', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.drop_column('sales_rep', 'totalLeadsManaged')
    op.add_column('hosts', sa.Column('assistantSignature', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('hosts', sa.Column('assistantName', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('hosts', 'salesRepSignature')
    op.drop_column('hosts', 'salesRepName')
    op.drop_column('gCredentials', 'credType')
    op.create_table('leads',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('salesRep', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('firstName', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('callTime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('interest', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('review', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('reviewReason', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('subject', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('threadId', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('msgIds', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('conversationText', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('sentEmailCount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('receivedEmailCount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lastEmailSentTime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('lastEmailReceivedTime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('company', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('latestReply', sa.TEXT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['salesRep'], [u'sales_rep.email'], name=u'leads_salesRep_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'leads_pkey')
    )
    op.drop_table('lead_threads')
    # ### end Alembic commands ###
