from models import User
from app import create_app
from app import db
import pytest
from config import TestConfig
from app.logic.commands.authentication import sign_up
from app.logic.commands.reviews import post_reviews
from app.logic.commands.product import post_product
from random import choice
import string

@pytest.fixture
def random_email():
    # returns a random email
    # random 5 character string
    return ''.join([choice(string.ascii_lowercase) for x in range(1,5)]) + "@isebarn.com"

@pytest.fixture
def valid_password():
    return "password123"

@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()   
        


@pytest.fixture
def user(app, random_email, valid_password):
    # creates a user using sign_up method in authentication.py
    # returns the user
    
    # create a user
    with app.app_context():
        sign_up(random_email, valid_password)
        user = User.query.filter_by(email=random_email).first()
        return user


# fixture for a product
# title, link, product_id, serpapi_link, rating, author, video, thumbnail
@pytest.fixture
def product():
    return {
        "title": "title",
        "link": "link",
        "product_id": "com.google.android.youtube",
        "serpapi_link": "serpapi_link",
        "rating": "rating",
        "author": "author",
        "video": "video",
        "thumbnail": "thumbnail"
    }


@pytest.fixture
def reviews():
    return [
        {
            "title": "Blue Icicle",
            "avatar": "https://play-lh.googleusercontent.com/a-/ACB-R5Qzg0SUBOVrrgqiBv_67u-ncKPrZJ5NINWp2OVMLg",
            "rating": 3.0,
            "snippet": "The UI has become annoying, when watching a video I can't just tap anywhere on the screen to get rid of all of the UI (play/pause, skip ahead, etc.), instead there has to be an X button in the corner. The UI doesn't go away after a certain amount of time either, making it required to press the X button. When I watch shorts there are also an annoying pause and skip button that don't go away. Plus I can't seek through the shorts.",
            "likes": 30705,
            "date": "March 10, 2023"
        },
        {
            "title": "John Reynolds",
            "avatar": "https://play-lh.googleusercontent.com/a-/ACB-R5S_k0aGgS2tKc1ro0HpqbOz8GUcP1mWbHKpRxIyP14",
            "rating": 3.0,
            "snippet": "I won't get into the issues with YouTube as a whole like everyone else. Instead, I'll report two issues that have been plaguing the mobile app for years: Whenever a video is paused for more than a couple seconds, when you unpause it, the video is ahead of the audio by about half a second for about 10 seconds, before it halts to let the audio catch up. Also, highlighting text blocks a large portion of the screen with an empty box while using the old text box, which still appears in a few places.",
            "likes": 1061,
            "date": "March 29, 2023"
        },
    ]

@pytest.fixture
def review_objects(app, user, product, reviews):
    # creates review objects and returns them
    with app.app_context():
        new_product = post_product(user, product)
        new_reviews = post_reviews(user, new_product.id, reviews)
        return new_reviews