"""removed email constraints from User

Revision ID: 65bed41a5bd7
Revises: ec20e299d82e
Create Date: 2020-07-10 02:06:54.144031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65bed41a5bd7'
down_revision = 'ec20e299d82e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('admin_email_key', 'admins', type_='unique')
    op.drop_constraint('client_email_key', 'clients', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('client_email_key', 'clients', ['email'])
    op.create_unique_constraint('admin_email_key', 'admins', ['email'])
    # ### end Alembic commands ###
