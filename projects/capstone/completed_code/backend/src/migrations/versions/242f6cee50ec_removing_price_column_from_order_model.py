"""removing price column from Order model

Revision ID: 242f6cee50ec
Revises: 970b869b675c
Create Date: 2020-07-08 19:23:31.897365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '242f6cee50ec'
down_revision = '970b869b675c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'total_price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('total_price', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
