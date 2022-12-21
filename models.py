# Models go here
from peewee import *

db = SqliteDatabase("betsy.db")

class User(Model):
    user_id = AutoField()
    name = CharField(unique=True)
    address = CharField(max_length=300)
    zip_postal_code = CharField()
    city = CharField(max_length=300)
    email = CharField(max_length=300, unique =True)
    
    class Meta:
        database = db
        table_name = 'User'

        
class Product(Model):
    product_id = AutoField()
    product_name = CharField(index=True, max_length=100)
    description = CharField(max_length=500)
    price_per_unit = DecimalField(
        max_digits=5, 
        decimal_places=2,
        auto_round=True)
    quantity = IntegerField(constraints=[Check('quantity>=1')])
    product_owner = ForeignKeyField(
        User, 
        field="user_id"
        )
    
    class Meta:
        database = db
        table_name = 'Product'
        

class Tag(Model):
    tag_id = AutoField()
    product_tags = CharField(max_length=300)
    product_name = ForeignKeyField(Product, field='product_name')
    
    
    
    class Meta:
        database = db
        table_name = 'Tag'
          
        
class Transaction(Model):
    transaction_id = AutoField()
    buyer = ForeignKeyField(User, field='name')
    seller = ForeignKeyField(Product, field='product_owner')
    product = ForeignKeyField(Product, field='product_id')
    item_quantity = IntegerField(constraints=[Check('item_quantity>=1')])
    
    class Meta:
        database = db
        table_name = 'Transaction'
        

    
    
    
