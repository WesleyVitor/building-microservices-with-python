
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from serializers import ProductAllOut, ProductIn
from repository.productRepository import ProductRepository
from mongoengine.queryset.queryset import QuerySet, BaseQuerySet
app = FastAPI()
app.add_middleware(CORSMiddleware)


@app.get("/")
async def index():
    productRepository:ProductRepository = ProductRepository()
    products:QuerySet = productRepository.get_all_products()
    return {"products":[ProductAllOut(name=product['name']) for product in products.as_pymongo()]}

@app.post("/")
async def create(product:ProductIn):
    productRepository:ProductRepository = ProductRepository()
    product = productRepository.create_product(product)
    return {"msg":"OK"}