__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
import pwd
from rich import print


# 1. Search
def search(term:str):
    query = (Product
             .select()
             .where(
        Product.product_name.contains(term) |
        Product.description.contains(term)))
    search_list = [product.product_name for product in query]  
    return f"Product Name: {search_list}"


# 2. List User Products 
def list_user_products(user_id:int):
    query = (Product
             .select()
             .where(Product.product_owner_id == user_id))
    product_list = [product.product_name for product in query]
    owner = [user.product_owner_id for user in query]
    return f"User: {set(owner)} | Item(s): {product_list}"

   
# 3. List Product Per Tag
def list_products_per_tag(tag_id:int):
    try:
        tag = Tag.get(Tag.tag_id == tag_id)
    except Tag.DoesNotExist:
        return "No Tag found with ID: {}".format(tag_id)
    products = (Product
                .select()
                .join(ProductTag)
                .join(Tag)
                # .where(Tag.tag== tag.tag))
                .where(Tag.tag_id== tag_id))
    product_list = [product.product_name for product in products]
    return f"Tag ID: {tag_id}  {product_list}"
# print(list_products_per_tag(5))


# 4. Add Product To Catalog
def add_product_to_catalog(
    user_id:int,
    product:str,
    description:str,
    price:float,
    qty:int,
    tag:str
    ):
    try:
        tags = Tag.get(Tag.tag == tag)
    except Tag.DoesNotExist:
        tags = Tag.create(tag=tag)
        # Select the row that contains user id's 
    user_id= (User
              .select()
              .where (User.user_id==user_id))
        # Create records in Product table   
    products = Product.create(
        product_owner=user_id,
        product_name=product.title(),
        description=description.capitalize(),
        price_per_unit=price,
        quantity=qty)
    products.product_tags.add(tags)
    products.save 
    return ('Product added to catalog!')


# 5. Update Stock
def update_stock(product_id:int, new_quantity:int):
        # Query the Product table
    query= (Product
        .update({Product.quantity: new_quantity})
        .where(Product.product_id == product_id))
    query.execute()
    return ('Stock updated!')


# 6. Purchase Product
def purchase_product(product_id:int, buyer_id:int, quantity:int):
    
    # Create The nescessary queary's
    buyer = (User.get(User.user_id == buyer_id))
    product_id= (Product.get(Product.product_id == product_id))
    seller = (Product.select().where(Product.product_id == product_id))
    for id in seller :
        if id.product_owner != buyer and quantity <= id.quantity:
            
            # Create records in Transaction table
            query = Transaction.create(
                buyer = buyer_id,
                seller = seller,
                product = product_id,
                item_quantity = quantity)
            query.save()
            
            # Update the quantity
            id.quantity -= quantity
            id.save()
            return(f"{buyer.name} Purchased {id.product_name}")
            
        elif id.product_owner == buyer:
            return('try another product please')    
        else:
            return(f"{id.product_name} is out of stock!")

        
# 7. Remove Product
def remove_product(product_id:int):
    obj = Product.get(Product.product_id == product_id)
    obj.product_tags
    obj.delete_instance(recursive=True)
    return ('Product removed!')



# 8. Function Collection
# print(search(''))
# print(list_user_products())
# print(list_products_per_tag())
# print(update_stock(1,14))
# print(purchase_product(1,3,4))
# print(remove_product())
