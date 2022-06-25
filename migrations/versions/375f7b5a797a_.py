"""empty message

Revision ID: 375f7b5a797a
Revises: d0ab3ebec918
Create Date: 2022-06-24 18:27:51.019682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '375f7b5a797a'
down_revision = 'd0ab3ebec918'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'token_expiration')
    op.drop_column('user', 'token')
    # ### end Alembic commands ###