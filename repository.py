from app import bcrypt
from models import User, App, Review, ReviewSummary
from app import db
from flask_jwt_extended import create_access_token
from serpapi import get_reviews
from openai_client import open_ai_summary

# get_product_summary uses get_reviews to get the top num reviews for a product
# and then uses openai to generate a summary of the reviews
def get_summary(package_name, num=10):

    # check if the app is already in the database
    if app:= App.query.filter_by(package_name=package_name).first():
        # check if the app has a summary in the database
        if summary:= ReviewSummary.query.filter_by(app_id=app.id).first():
            # return the summary if it exists
            return summary.summary

    # get the top num reviews for the product
    reviews = get_reviews(package_name, num)
    reviews = reviews['reviews']
    
    
    # get the text of the reviews
    reviews_text = [review['snippet'] for review in reviews]

    # use openai to generate a summary of the reviews
    summary_prompt = "Write a summary of the following reviews: {}".format("\n".join(reviews_text))
    summary = open_ai_summary(summary_prompt)

    # add the app to the database
    app = App(package_name=package_name)
    db.session.add(app)
    db.session.commit()

    # add the reviews to the database
    for review in reviews:
        review = Review(review=review['snippet'], app_id=app.id)
        db.session.add(review)

    # add the summary to the database
    summary = ReviewSummary(summary=summary, app_id=app.id)
    db.session.add(summary)

    # commit the changes to the database
    db.session.commit()

    return summary.summary
