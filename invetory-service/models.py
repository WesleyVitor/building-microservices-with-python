import mongoengine as models
models.connect(host="mongodb://172.18.0.2:27017/inventory")


class Product(models.Document):
    name = models.StringField(max_length=255)
    price = models.DecimalField()
    description = models.StringField(max_length=500)

    