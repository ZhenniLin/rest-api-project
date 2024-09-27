"""empty message

Revision ID: 729306fc777f
Revises: 8c932cab3c4c
Create Date: 2024-09-26 17:27:37.596977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '729306fc777f'
down_revision = '8c932cab3c4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
