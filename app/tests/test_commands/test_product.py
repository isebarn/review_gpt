
from app.logic.commands.product import post_product


def test_post_product(user, product):
    # products have the following properties
    # title, link, product_id, serpapi_link, rating, author, video, thumbnail, user_id

    # save the product to the database
    product = post_product(user, product)

    # check if the product was saved to the database
    assert product.id

def test_post_product_exists(user, product):
    # products have the following properties
    # title, link, product_id, serpapi_link, rating, author, video, thumbnail, user_id

    # save the product to the database
    product_original = post_product(user, product)

    # check if the product was saved to the database
    assert product_original.id  

    # save the product to the database
    product_exists = post_product(user, product)

    # check if the product was saved to the database
    assert product_original.id == product_exists.id    
