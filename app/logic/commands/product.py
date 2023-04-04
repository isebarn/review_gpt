# import the product and user model
from models import Product
from models import db

# save app to the database
def post_product(user, product):
    # first check if the product exists with product_id and user_id
    if product_exists := Product.query.filter_by(product_id=product['product_id'], user_id=user.id).first():
        return product_exists

    product = Product(**product, user_id=user.id)

    # save the product to the database
    db.session.add(product)
    db.session.commit()

    return product
