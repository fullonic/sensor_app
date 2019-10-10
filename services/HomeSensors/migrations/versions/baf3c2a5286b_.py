"""empty message

Revision ID: baf3c2a5286b
Revises: 
Create Date: 2019-10-09 14:14:24.156503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baf3c2a5286b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sensors', sa.Column('frequency', sa.Float(precision=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sensors', 'frequency')
    # ### end Alembic commands ###
