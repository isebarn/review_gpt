from models import Product, Review
from models import db
from app.logic.queries.product import get_product
from datetime import datetime

# get all reviews for an product
def get_reviews(user, product_id):
    product = Product.query.filter_by(id=product_id, user_id=user.id).first()
    reviews = Review.query.filter_by(product_id=product.id).all()

    return reviews

# save a list of reviews to the database
def post_reviews(user, product_id, reviews):
    product = get_product(user, product_id)

    for review in reviews:

        # convert isostring to datetime
        dt = datetime.fromisoformat(review['date'])
        review['date'] = dt

        review_id = review['avatar'].split('/')[-1]
        if Review.query.filter_by(review_id=review_id, product_id=product.id).first():
            continue

        new_review = Review(**review, review_id=review['avatar'].split('/')[-1], product_id=product.id)
        db.session.add(new_review)
        db.session.commit()

    return get_reviews(user, product_id)