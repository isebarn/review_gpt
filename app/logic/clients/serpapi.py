import app.logic.commands.product as product
from requests import get
import app

SERP_API_URL = "https://serpapi.com/search.json"


# search for a product on google play
def search_product(search):
    params = {
        "engine": "google_play",
        "store": "apps",
        "q": search,
        "api_key": app.Config.SERP_API_KEY
    }

    search = get(SERP_API_URL, params=params)
    results = search.json()
    return results


# get data from google search reviews
def get_reviews(product_id, num=100):
    params = {
        "engine": "google_play_product",
        "store": "apps",
        "product_id": product_id,
        "all_reviews": True,
        "num": num,
        "api_key": app.Config.SERP_API_KEY
    }
    
    search = get(SERP_API_URL, params=params)
    results = search.json()
    return results