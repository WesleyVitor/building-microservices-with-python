
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from serializers import ProductAllOut, ProductIn, ProductOut
from repository.productRepository import ProductRepository
from mongoengine.queryset.queryset import QuerySet
from utils.id_validation import PyObjectId
from bson.objectid import ObjectId
app = FastAPI()
app.add_middleware(CORSMiddleware)

@app.get("/")
async def index():
    productRepository:ProductRepository = ProductRepository()
    products:QuerySet = productRepository.get_all_products()
    return {"products":[ProductAllOut(_id=str(product['_id']),name=product['name'],
     description=product['description']) for product in products.as_pymongo()]}
    
@app.post("/")
async def create(product:ProductIn):
    productRepository:ProductRepository = ProductRepository()
    try:
        product = productRepository.create_product(product)
        return JSONResponse({"msg":"Tudo OK!"}, status.HTTP_201_CREATED)
    except:
        return JSONResponse({"msg":"Alguma coisa deu errado!"}, status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.delete("/{objectID}")
async def deletar(objectID: PyObjectId):
    productRepository:ProductRepository = ProductRepository()
    try:
        productRepository.delete_one_product(objectID)
        return JSONResponse({"msg":"Tudo OK!"}, status.HTTP_200_OK)
    except:
        return JSONResponse({"msg":"Alguma coisa deu errado!"}, status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get("/{objectID}")
async def show(objectID:PyObjectId):
    productRepository:ProductRepository = ProductRepository()
    product:QuerySet = productRepository.get_one_product(objectID)
    print(product)
    return {"product":ProductOut(name=product['name'], description=product['description'], price=product['price'])}