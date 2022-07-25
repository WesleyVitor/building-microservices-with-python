from models import Product

class ProductRepository:

    def get_all_products(self):
        """ return all products"""
        return Product.objects().all()
    
    def create_product(self, product):
        """ Register a product """
        product:Product = Product(name=product.name, price=product.price, description=product.description)
        product.save()
        return product