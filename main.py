__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *

def search(term):
    search_list=[]
    query = (Product
             .select()
             .where(
        Product.product_name.contains(term) |
        Product.description.contains(term)))
    for q in query:
        search_list.append(q.product_name)    
    return "Product Name: {}".format(search_list)
    
# print(search('')) 

def list_user_products(user_id):
    product_list = []
    query = (Product
             .select()
             .where(Product.product_owner_id == user_id))
    for q in query:
        product_list.append(q.product_name)
    return "UserID: {}  |   Item(s): {}".format(q.product_owner, product_list)      
# print(list_user_products())

def list_products_per_tag(tag_id):
    product_list = []
    query = (Tag
             .select()
             .where (Tag.tag_id==tag_id))
    for q in query:
        product_list.append(q.product_name.product_name)
    return "Product List: {}".format(product_list)
# print(list_products_per_tag())

def add_product_to_catalog(
    user_id: int,
    product: str,
    description: str,
    price: float,
    qty:int,
    product_tags:str
    ):
    # adding product to catalog
    user_id= (User
              .select()
              .where (User.user_id==user_id))
    query0=Product.create(
        product_owner=user_id,
        product_name=product.title(),
        description=description.capitalize(),
        price_per_unit=price,
        quantity=qty
        )
    # adding related tags to ptoduct
    query1=Tag.create(
        product_name = product.title(),
        product_tags = product_tags,   
    )
    query0.save()
    query1.save()
    return ('Product added to catalog!')

# print(add_product_to_catalog(
#     user_id=1,
#     product='',
#     description='',
#     product_tags=(''),
#     price=,
#     qty=))


def update_stock(product_id, new_quantity):
    query= (Product
        .update({Product.quantity: new_quantity})
        .where(Product.product_id == product_id))
    query.execute()
    return ('Stock updated!')
# print(update_stock())


def purchase_product(product_id: int, buyer_id: int, quantity: int):
    
    buyer_id = (User
        .select(User.user_id)
        .where((User.user_id == buyer_id)))
    
    seller = (Product
        .select(Product.product_owner)
        .where(Product.product_id == product_id))
    
    product_id= (Product
        .select(Product.product_id)
        .where ((Product.product_id == product_id)))
    
    query = Transaction.create(
        buyer = buyer_id,
        seller = seller,
        product = product_id,
        item_quantity = quantity
    )
    query.save()
    return ('Purchased Product!')
# purchase_product()


def remove_product(product_id):
    obj = Product.get(Product.product_id == product_id)
    obj.delete_instance(recursive=True)
    return ('Product removed!')
# remove_product()
