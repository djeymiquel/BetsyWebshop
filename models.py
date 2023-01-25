# Models go here
from peewee import *

db = SqliteDatabase("betsy.db")


class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = AutoField()
    name = CharField(unique=True)
    address = CharField(max_length=255)
    zip_postal_code = CharField(max_length=6)
    city = CharField(max_length=255)
    email = CharField(max_length=255, unique =True)
  
class Tag(BaseModel):
    tag_id = AutoField()
    tag = CharField(max_length=255)
    

class Product(BaseModel):
    product_id = AutoField()
    product_name = CharField(index=True)
    description = CharField(max_length=255)
    price_per_unit = DecimalField(max_digits=5, decimal_places=2, auto_round=True)
    quantity = IntegerField()
    product_tags = ManyToManyField(Tag)
    product_owner = ForeignKeyField(User, field="user_id")
    
ProductTag = Product.product_tags.get_through_model()

class Transaction(BaseModel):
    transaction_id = AutoField()
    buyer = ForeignKeyField(User, field='user_id')
    product = ForeignKeyField(Product, field='product_id')
    item_quantity = IntegerField()
