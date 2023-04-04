# import the product and user model
from models import Product, ProductMessage
from models import db

def get_product_messages(user, product_id):
    # get all product messages
    if Product.query.filter_by(id=product_id, user_id=user.id).first():
        product_messages = ProductMessage.query.filter_by(product_id=product_id).order_by(ProductMessage.id.desc()).all()
        return product_messages

def post_product_message(product, message):
    # create a new product message
    product_message = ProductMessage(**message, product_id=product.id)
    # save the product message
    db.session.add(product_message)
    db.session.commit()
    return product_message