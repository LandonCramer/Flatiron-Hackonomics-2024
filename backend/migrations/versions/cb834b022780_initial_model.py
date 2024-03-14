"""initial model

Revision ID: cb834b022780
Revises: 
Create Date: 2024-03-14 15:42:56.155592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb834b022780'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accounts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('bank_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('account_number', sa.VARCHAR(length=100), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_accounts_user_id_users'),
    sa.PrimaryKeyConstraint('id', name='pk_accounts')
    )
    # ### end Alembic commands ###
