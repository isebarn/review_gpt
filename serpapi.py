import app
from requests import get

SERP_API_URL = "https://serpapi.com/search.json"

# get data from google search reviews
def get_reviews(package_name, num=40):
    params = {
        "engine": "google_play_product",
        "store": "apps",
        "product_id": package_name,
        "all_reviews": True,
        "num": num,
        "api_key": app.app.config['SERP_API_KEY']
    }
    
    search = get(SERP_API_URL, params=params)
    results = search.json()
    return results