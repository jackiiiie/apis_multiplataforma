# src/service/product_service.py

import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.insert(0, root_dir)
from sqlalchemy.orm import Session
from src.domain.model.models import Product
from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoUpdateDTO

def create(db_session: Session, data: ProdutoCreateDTO):
    new_product = Product(name=data.name, price=data.price, description=data.description, category=data.category)
    db_session.add(new_product)
    db_session.commit()
    db_session.refresh(new_product)
    return new_product

def find_by_id(db_session: Session, product_id: int):
    return db_session.query(Product).filter(Product.id == product_id).first()

def find_all(db_session: Session):
    return db_session.query(Product).all()

def update(db_session: Session, product_id: int, product_data: ProdutoUpdateDTO):
    product = db_session.query(Product).filter(Product.id == product_id).first()
    if product:
        for key, value in product_data.dict(exclude_unset=True).items():
            setattr(product, key, value)
        db_session.commit()
        db_session.refresh(product)
    return product

def delete(db_session: Session, product_id: int):
    product = db_session.query(Product).filter(Product.id == product_id).first()
    if product:
        db_session.delete(product)
        db_session.commit()
        return product.id
    return None















# import sys
# import os

# # Adiciona o diretório raiz do projeto ao sys.path
# current_dir = os.path.dirname(__file__)
# root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
# sys.path.insert(0, root_dir)

# from sqlalchemy.orm import Session
# from src.domain.model.models import Product
# from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoUpdateDTO

# def create(db_session: Session, data: ProdutoCreateDTO):
#     new_product = Product(name=data.name, price=data.price, description=data.description, category=data.category)
#     db_session.add(new_product)
#     db_session.commit()
#     db_session.refresh(new_product)
#     return new_product

# def find_by_id(db_session: Session, product_id: int):
#     return db_session.query(Product).filter(Product.id == product_id).first()

# def find_all(db_session: Session):
#     return db_session.query(Product).all()

# def update(db_session: Session, product_id: int, product_data: ProdutoUpdateDTO):
#     product = db_session.query(Product).filter(Product.id == product_id).first()
#     if product:
#         for key, value in product_data.dict(exclude_unset=True).items():
#             setattr(product, key, value)
#         db_session.commit()
#         db_session.refresh(product)
#     return product

# def delete(db_session: Session, product_id: int):
#     product = db_session.query(Product).filter(Product.id == product_id).first()
#     if product:
#         db_session.delete(product)
#         db_session.commit()
#         return product.id
#     return None



# ///////////////////////////
# import logging

# from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoDTO, ProdutoUpdateDTO
# from src.repository.usuario_repository import ProductRepository


# class ProductService:

#     def __init__(self, repository: ProductRepository):
#         self.repository = repository

#     def create(self, data: ProdutoCreateDTO) -> ProdutoDTO:
#         logging.info('Criando produto')
#         # TODO: implementar método
#         pass

#     def find_by_id(self, user_id: int) -> ProdutoDTO:
#         logging.info(f'Buscando produto com ID {user_id}')
#         # TODO: implementar método
#         pass

#     def find_all(self) -> list[ProdutoDTO]:
#         logging.info('Buscando todos os produtos')
#         # TODO: implementar método
#         pass

#     def update(self, user_id: int, user_data: ProdutoUpdateDTO) -> ProdutoDTO:
#         logging.info(f'Atualizando produto com ID {user_id}')
#         # TODO: implementar método
#         pass

#     def delete(self, user_id: int) -> int:
#         logging.info(f'Deletando produto com ID {user_id}')
#         # TODO: implementar método
#         pass
