"""empty message

Revision ID: 13d856443274
Revises: 
Create Date: 2023-04-27 18:08:31.974959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13d856443274'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('follower_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], name='follows_follower_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='follows_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='follows_pkey')
    )
    # ### end Alembic commands ###
