from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Order
from serializers import OrderIn, OrderOut
import requests
app = FastAPI()
app.add_middleware(CORSMiddleware)

@app.get("/orders/")
async def index():
    orders = Order.objects().all().as_pymongo()

    return {"orders":[OrderOut(product=str(order['product']),amount=order['amount'],
     price_all=order['price_all'], status=order['status']) for order in orders.as_pymongo()]}

@app.post("/orders/")
async def create(order:OrderIn):
    order = dict(order)

    #Comunicação síncrona com o microsserviço de inventário
    response:requests.Response = requests.get(f"http://127.0.0.1:8000/products/{order['product']}")
    product = response.json()
    
    if(product != None):
        #Salvar ordem
        order = Order(
            product = order["product"],
            amount= order["amount"],
            price_all= float(product['product']['price'])*order["amount"],
            status="complete"
        )
        order.save()
        return {"msg":"OK!"}
    else:
        return {"msg":"Produto não existe!"}

