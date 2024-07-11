import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.insert(0, root_dir)

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.config.database import SessionLocal, engine
from src.domain.dto.dtos  import ProdutoCreateDTO, ProdutoUpdateDTO, Product
from src.service.product_service import create, find_by_id, find_all, update, delete
from src.controller.auth_controller import get_current_user

router = APIRouter()

# Middleware para obter a sessão do banco de dados
def get_db_session():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

# ... Definição dos endpoints usando os serviços ...

@router.post('/products', response_model=Product)
async def create_product(product: ProdutoCreateDTO, db: Session = Depends(get_db_session), current_user: str = Depends(get_current_user)):
    return create(db, product)

@router.get('/products/{id}', response_model=Product)
async def get_product(id: int, db: Session = Depends(get_db_session), current_user: str = Depends(get_current_user)):
    product = find_by_id(db, id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get('/products', response_model=List[Product])
async def list_products(db: Session = Depends(get_db_session), current_user: str = Depends(get_current_user)):
    return find_all(db)

@router.put('/products/{id}', response_model=Product)
async def update_product(id: int, updated_product: ProdutoUpdateDTO, db: Session = Depends(get_db_session), current_user: str = Depends(get_current_user)):
    product = update(db, id, updated_product)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete('/products/{id}', response_model=int)
async def delete_product(id: int, db: Session = Depends(get_db_session), current_user: str = Depends(get_current_user)):
    product_id = delete(db, id)
    if not product_id:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_id


# import sys
# import os

# # Adiciona o diretório raiz do projeto ao sys.path
# current_dir = os.path.dirname(__file__)
# root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
# sys.path.insert(0, root_dir)

# from sqlalchemy.orm import Session
# from src.domain.model.models  import Product
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



# import sys
# import os

# # Adiciona o diretório raiz do projeto ao sys.path
# current_dir = os.path.dirname(__file__)
# root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
# sys.path.insert(0, root_dir)



# import logging
# from fastapi import HTTPException
# from pydantic import TypeAdapter
# from sqlalchemy.exc import IntegrityError

# from src.domain.dto.dtos import ProductCreateDTO, ProductDTO, ProductUpdateDTO
# from src.repository.usuario_repository import ProductRepository
# from src.domain.model.models import Product

# class ProductService:

#     def __init__(self, product_repository: ProductRepository):
#         self.product_repository = product_repository

#     def create(self, product_data: ProductCreateDTO) -> ProductDTO:
#         logging.info('Criando um novo produto.')
#         product = Product(**product_data.model_dump())
#         try:
#             created = self.product_repository.create(product)
#             return TypeAdapter(ProductDTO).validate_python(created)
#         except IntegrityError as e:
#             logging.error(f'Erro ao criar o produto: {product_data.model_dump()}')
#             raise HTTPException(status_code=409, detail=f'Produto já existe na base: {e.args[0]}')
    
    
#     def read(self, product_id: int) -> ProductDTO:
#         logging.info('Buscando um produto.')
#         return TypeAdapter(ProductDTO).validate_python(self._read(product_id))

#     def _read(self, product_id: int) -> Product:
#         product = self.product_repository.read(product_id)
#         if product is None:
#             logging.error(f'Produto {product_id} não encontrado.')
#             raise HTTPException(status_code=404, detail=f'Produto {product_id} não encontrado.')
#         return product

#     def find_all(self) -> list[ProductDTO]:
#         logging.info('Buscando todos os produtos.')
#         products = self.product_repository.find_all()
#         return [TypeAdapter(ProductDTO).validate_python(product) for product in products]

#     def update(self, product_id: int, product_data: ProductUpdateDTO):
#         logging.info(f'Atualizando o produto {product_id}.')
#         product = self._read(product_id)
#         product_data = product_data.model_dump(exclude_unset=True)
#         for key, value in product_data.items():
#             setattr(product, key, value)
#         updated_product = self.product_repository.create(product)
#         logging.info(f'Produto {product_id} atualizado: {updated_product}')
#         return TypeAdapter(ProductDTO).validate_python(updated_product)

#     def delete(self, product_id: int) -> int:
#         product = self._read(product_id)
#         self.product_repository.delete(product)
#         logging.info(f'Produto {product_id} deletado')
#         return product_id


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
