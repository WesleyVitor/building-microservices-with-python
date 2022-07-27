from models import Product
from mongoengine.queryset.queryset import QuerySet
class ProductRepository:

    def get_all_products(self):
        """ return all products"""
        return Product.objects().all()
    
    def create_product(self, product):
        """ Register a product """
        product:Product = Product(name=product.name, price=product.price, description=product.description)
        product.save()
        return product
    
    def delete_one_product(self, id):
        """ Delete one product """
        product = Product.objects(id=id).as_pymongo()
        product.delete()

    def get_one_product(self, id):
        """ Return one product """
        return Product.objects(id=id).as_pymongo().first()
    
    def update_one_product(self, id, product_new):
        """ Atualiza as informações de um produto"""
        product:QuerySet = Product.objects(id=id).as_pymongo()
        
        product.update(name=product_new.name, description=product_new.description, price=product_new.price)