"""Add historic models

Revision ID: a6ad14a4422a
Revises: baf3c2a5286b
Create Date: 2019-10-10 18:02:13.415146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6ad14a4422a'
down_revision = 'baf3c2a5286b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('historic_humidity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hour', sa.Integer(), nullable=False),
    sa.Column('day', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('unit', sa.String(length=4), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historic_temperature',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hour', sa.Integer(), nullable=False),
    sa.Column('day', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('unit', sa.String(length=4), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('ldr', sa.Column('hour', sa.DateTime(), nullable=True))
    op.add_column('temp_hum', sa.Column('hour', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('temp_hum', 'hour')
    op.drop_column('ldr', 'hour')
    op.drop_table('historic_temperature')
    op.drop_table('historic_humidity')
    # ### end Alembic commands ###
