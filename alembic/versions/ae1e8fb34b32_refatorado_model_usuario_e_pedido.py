"""Refatorado model Usuario e Pedido

Revision ID: ae1e8fb34b32
Revises: 2248a32fa866
Create Date: 2023-11-01 21:15:06.976276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae1e8fb34b32'
down_revision: Union[str, None] = '2248a32fa866'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('produto_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_pedido_produto', 'produto', ['produto_id'], ['id'])
        batch_op.create_foreign_key('fk_pedido_usuario', 'usuario', ['usuario_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.drop_constraint('fk_pedido_usuario', type_='foreignkey')
        batch_op.drop_constraint('fk_pedido_produto', type_='foreignkey')
        batch_op.drop_column('produto_id')
        batch_op.drop_column('usuario_id')

    # ### end Alembic commands ###
