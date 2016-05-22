"""alter db

Revision ID: d6019e611353
Revises: None
Create Date: 2016-05-09 11:38:02.281703

"""

# revision identifiers, used by Alembic.
revision = 'd6019e611353'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'fk_contract_id_caluclation', 'calculation', type_='foreignkey')
    op.create_foreign_key('fk_contract_id_caluclation', 'calculation', 'contract', ['contract_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.drop_constraint(u'fk_photo_upload_id_employee', 'employee', type_='foreignkey')
    op.create_foreign_key('fk_photo_upload_id_employee', 'employee', 'upload', ['photo_upload_id'], ['id'], onupdate='cascade', ondelete='restrict')
    op.drop_constraint(u'fk_maintainer_id_resource', 'resource', type_='foreignkey')
    op.drop_constraint(u'fk_structure_id_resource', 'resource', type_='foreignkey')
    op.create_foreign_key('fk_maintainer_id_resource', 'resource', 'employee', ['maintainer_id'], ['id'], onupdate='cascade', ondelete='restrict', use_alter=True)
    op.drop_column('resource', 'structure_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resource', sa.Column('structure_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint('fk_maintainer_id_resource', 'resource', type_='foreignkey')
    op.create_foreign_key(u'fk_structure_id_resource', 'resource', 'structure', ['structure_id'], ['id'], onupdate=u'CASCADE', ondelete=u'RESTRICT')
    op.create_foreign_key(u'fk_maintainer_id_resource', 'resource', 'employee', ['maintainer_id'], ['id'])
    op.drop_constraint('fk_photo_upload_id_employee', 'employee', type_='foreignkey')
    op.create_foreign_key(u'fk_photo_upload_id_employee', 'employee', 'upload', ['photo_upload_id'], ['id'])
    op.drop_constraint('fk_contract_id_caluclation', 'calculation', type_='foreignkey')
    op.create_foreign_key(u'fk_contract_id_caluclation', 'calculation', 'contract', ['contract_id'], ['id'])
    ### end Alembic commands ###