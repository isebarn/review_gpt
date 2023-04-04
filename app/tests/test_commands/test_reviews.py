from app.logic.commands.reviews import get_reviews, post_reviews
from app.logic.commands.product import post_product

def test_get_reviews(user, product, reviews):
    product = post_product(user, product)
    reviews_result = get_reviews(user, product.id)

    assert not any(reviews_result)

    new_reviews = post_reviews(user, product.id, reviews)

    assert len(new_reviews) == len(reviews)
