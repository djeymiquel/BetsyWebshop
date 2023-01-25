from models import *
from main import add_product_to_catalog

# Connect db and create tables
db.connect()
db.create_tables([User, Product, Tag, Transaction, ProductTag])

    # Populate database with test data   
def populate_test_database(name:str, address:str, zip_postal_code:str, city:str, email:str):
    query = User.create(
        name = name.title(), 
        address = address.capitalize(), 
        zip_postal_code = zip_postal_code.upper(), 
        city = city.title(), 
        email = email )
    query.save()

populate_test_database(
    name="bob", 
    address='stierstraat 1', 
    zip_postal_code='2345ab', 
    city='Amsterdam', 
    email='bob@gmail.com')

populate_test_database(
    name="julia", 
    address='hartstraat 2', 
    zip_postal_code='7693hc', 
    city='Enschede', 
    email='julia@gmail.com')

populate_test_database(
    name="luis", 
    address='grootstraat 3', 
    zip_postal_code='2560yo', 
    city='Almere', 
    email='luis@gmail.com')

populate_test_database(
    name="clare", 
    address='breedstraat 4', 
    zip_postal_code='1378nm', 
    city='Groningen', 
    email='clare@gmail.com')


    # Add product to catalog
print(add_product_to_catalog(
    user_id=2,
    product='chair',
    description='comfortable chair',
    tag ='furniture',
    price=70,
    qty=4))

print(add_product_to_catalog(
    user_id=1,
    product='couch',
    description='soft couch',
    tag ='furniture',
    price=450.0,
    qty=2))

print(add_product_to_catalog(
    user_id=4,
    product='Nike Airmax',
    description='new shoes',
    tag ='sneakers',
    price=80.0,
    qty=2))

print(add_product_to_catalog(
    user_id=2,
    product='tablet',
    description='cool tablet',
    tag ='media',
    price=200.0,
    qty=4))

# close conection 
db.close()