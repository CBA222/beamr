"""empty message

Revision ID: 17e88fb15b0c
Revises: 973b67a547f6
Create Date: 2020-09-13 07:19:22.400131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17e88fb15b0c'
down_revision = '973b67a547f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('channel')
    op.add_column('user_account', sa.Column('channel_icon_url', sa.String(length=128), nullable=True))
    op.add_column('user_account', sa.Column('channel_url', sa.String(length=128), nullable=True))
    op.add_column('user_account', sa.Column('name', sa.String(length=128), nullable=True))
    op.add_column('user_account', sa.Column('subscriber_count', sa.Integer(), nullable=True))
    op.drop_constraint('video_channel_id_fkey', 'video', type_='foreignkey')
    op.create_foreign_key(None, 'video', 'user_account', ['channel_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'video', type_='foreignkey')
    op.create_foreign_key('video_channel_id_fkey', 'video', 'channel', ['channel_id'], ['id'])
    op.drop_column('user_account', 'subscriber_count')
    op.drop_column('user_account', 'name')
    op.drop_column('user_account', 'channel_url')
    op.drop_column('user_account', 'channel_icon_url')
    op.create_table('channel',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('channel_url', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('channel_icon_url', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=128), autoincrement=False, nullable=True),
    sa.Column('subscriber_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='channel_pkey')
    )
    # ### end Alembic commands ###
