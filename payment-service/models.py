from mongoengine import *
connect(host="mongodb://172.18.0.2:27017/payment")

class Order(Document):
    product = StringField()
    amount = IntField(min_value=1)
    price_all = DecimalField()
    status = StringField()