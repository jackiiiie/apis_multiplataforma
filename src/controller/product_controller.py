import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
current_dir = os.path.dirname(__file__)
root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.insert(0, root_dir)


from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Modelo de Produto
class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str = None

# Simulação de banco de dados em memória
fake_db = []

@router.post('/products', response_model=Product)
async def create_product(product: Product):
    fake_db.append(product)
    return product

@router.get('/products/{id}', response_model=Product)
async def get_product(id: int):
    product = next((p for p in fake_db if p.id == id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get('/products', response_model=List[Product])
async def list_products():
    return fake_db

@router.put('/products/{id}', response_model=Product)
async def update_product(id: int, updated_product: Product):
    for idx, product in enumerate(fake_db):
        if product.id == id:
            fake_db[idx] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

@router.delete('/products/{id}', response_model=Product)
async def delete_product(id: int):
    for idx, product in enumerate(fake_db):
        if product.id == id:
            del fake_db[idx]
            return product
    raise HTTPException(status_code=404, detail="Product not found")












# from fastapi import APIRouter, Depends

# from src.config.dependencies import get_authenticated_user, get_product_service
# from src.domain.dto.dtos import ProdutoCreateDTO, ProdutoUpdateDTO
# from src.service.product_service import ProductService

# product_router = APIRouter(prefix='/products', tags=['Products'], dependencies=[Depends(get_authenticated_user)])


# # TODO: utilizar as anotações adequadamente
# async def create(request: ProdutoCreateDTO, service: ProductService = Depends(get_product_service)):
#     return service.create(request)


# # TODO: implementar método para buscar produto por ID
# async def find_by_id(user_id: int, service: ProductService = Depends(get_product_service)):
#     return service.find_by_id(user_id=user_id)


# # TODO: implementar método para buscar todos os produtos
# async def find_all(service: ProductService = Depends(get_product_service)):
#     return service.find_all()


# # TODO: implementar método para atualizar produto
# async def update(user_id: int, user_data: ProdutoUpdateDTO, service: ProductService = Depends(get_product_service)):
#     return service.update(user_id, user_data)


# # TODO: implementar método para deletar produto
# async def delete(user_id: int, service: ProductService = Depends(get_product_service)):
#     service.delete(user_id=user_id)
