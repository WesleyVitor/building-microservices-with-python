from pydantic import BaseModel, Field
from utils.id_validation import PyObjectId

class ProductAllOut(BaseModel):
    id:str = Field(alias='_id')
    name:str
    description:str

class ProductIn(BaseModel):
    name:str
    price:str
    description:str

class ProductOut(BaseModel):
    name:str
    description:str
    price:str

class ProductUpdate(BaseModel):
    name:str
    description:str
    price:str