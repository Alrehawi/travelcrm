"""alter db

Revision ID: 9d6e4f7a0f93
Revises: b1eac8a9f577
Create Date: 2016-08-15 20:24:36.483777

"""

# revision identifiers, used by Alembic.
revision = '9d6e4f7a0f93'
down_revision = 'b1eac8a9f577'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('html_content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], name='fk_resource_id_mail', onupdate='cascade', ondelete='restrict'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', name='unique_idx_name_mail')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mail')
    ### end Alembic commands ###
