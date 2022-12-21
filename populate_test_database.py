from models import *

db.create_tables([User, Product, Tag, Transaction]) 

def populate_test_database(name , address, zip_postal_code, city, email):
    query = User.create(name=name.title() , address=address.capitalize() , zip_postal_code=zip_postal_code.upper(), city = city.title(), email = email )
    query.save()
    
populate_test_database(name="bob" , address='stierstraat 1', zip_postal_code='2345ab', city='Amsterdam', email='bob@gmail.com')
populate_test_database(name="julia", address='hartstraat 2', zip_postal_code='7693hc', city='Enschede', email='julia@gmail.com')
populate_test_database(name="luis", address='grootstraat 3', zip_postal_code='2560yo', city='Almere', email='luis@gmail.com')
populate_test_database(name="clare", address='breedstraat 4', zip_postal_code='1378nm', city='Groningen', email='clare@gmail.com')