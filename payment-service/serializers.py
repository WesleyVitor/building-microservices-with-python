from pydantic import BaseModel

class OrderIn(BaseModel):
    product:str
    amount:int

class OrderOut(BaseModel):
    product:str
    amount:int
    price_all:str
    status:str
