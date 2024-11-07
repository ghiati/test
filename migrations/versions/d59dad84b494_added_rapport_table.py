"""Added Rapport table

Revision ID: d59dad84b494
Revises: 0d20eb0d8eb1
Create Date: 2024-11-06 10:26:45.428718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd59dad84b494'
down_revision = '0d20eb0d8eb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rapport',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=10000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=100),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=200),
               nullable=True)

    op.drop_table('rapport')
    # ### end Alembic commands ###
