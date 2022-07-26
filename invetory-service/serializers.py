from pydantic import BaseModel, Field
from utils.id_validation import PyObjectId

class ProductAllOut(BaseModel):
    #id:PyObjectId = Field(..., alias='_id')
    name:str
    description:str

class ProductIn(BaseModel):
    name:str
    price:str
    description:str