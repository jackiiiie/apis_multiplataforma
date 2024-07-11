import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.insert(0, root_dir)
from sqlalchemy import Column, Integer, String, Float

from src.config.database import Base
from src.config.database import init_db


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(50))
    descricao = Column(String(255))
    preco = Column(Float)
    estoque = Column(Integer)

    def __repr__(self):
        return f'<Produto(id={self.id}, nome={self.nome}, descricao={self.descricao}, preco={self.preco}, estoque={self.estoque})>'


init_db()
