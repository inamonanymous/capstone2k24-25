"""empty message

Revision ID: 2098285f9f09
Revises: 96902cd9cf04
Create Date: 2024-10-10 18:01:57.219758

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2098285f9f09'
down_revision = '96902cd9cf04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('formresponses', schema=None) as batch_op:
        batch_op.alter_column('form_id',
               existing_type=mysql.VARCHAR(length=32),
               nullable=True)
        batch_op.alter_column('user_id',
               existing_type=mysql.VARCHAR(length=32),
               nullable=True)

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo_path', sa.String(length=255), nullable=True))
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', mysql.VARCHAR(length=255), nullable=True))
        batch_op.drop_column('photo_path')

    with op.batch_alter_table('formresponses', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=mysql.VARCHAR(length=32),
               nullable=False)
        batch_op.alter_column('form_id',
               existing_type=mysql.VARCHAR(length=32),
               nullable=False)

    # ### end Alembic commands ###
