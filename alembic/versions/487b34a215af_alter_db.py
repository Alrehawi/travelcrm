"""alter db

Revision ID: 487b34a215af
Revises: 4327c5c76f29
Create Date: 2014-04-12 18:54:58.337110

"""

# revision identifiers, used by Alembic.
revision = '487b34a215af'
down_revision = '4327c5c76f29'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tour', sa.Column('end_date', sa.Date(), nullable=False))
    op.add_column('tour', sa.Column('start_date', sa.Date(), nullable=False))
    op.drop_column('tour', 'start_dt')
    op.drop_column('tour', 'end_dt')
    op.add_column('tour_point', sa.Column('end_date', sa.Date(), nullable=False))
    op.add_column('tour_point', sa.Column('start_date', sa.Date(), nullable=False))
    op.drop_column('tour_point', 'start_dt')
    op.drop_column('tour_point', 'end_dt')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tour_point', sa.Column('end_dt', postgresql.TIMESTAMP(), nullable=False))
    op.add_column('tour_point', sa.Column('start_dt', postgresql.TIMESTAMP(), nullable=False))
    op.drop_column('tour_point', 'start_date')
    op.drop_column('tour_point', 'end_date')
    op.add_column('tour', sa.Column('end_dt', postgresql.TIMESTAMP(), nullable=False))
    op.add_column('tour', sa.Column('start_dt', postgresql.TIMESTAMP(), nullable=False))
    op.drop_column('tour', 'start_date')
    op.drop_column('tour', 'end_date')
    ### end Alembic commands ###