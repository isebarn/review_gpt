# import the product and user model
from models import Product


# get all products for a user
def get_products(user):
    # get all the products for a user
    products = Product.query.filter_by(user_id=user.id).all()

    return products

# get product by id
def get_product(user, id):
    # get the product
    product = Product.query.filter_by(id=id, user_id=user.id).first()

    return product