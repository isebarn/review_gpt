from datetime import datetime
import app.logic.commands.product as product
from requests import get
import app
from textblob import TextBlob

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

    # convert every item['date'] in results from 'April 10, 2023'  to iso string
    for item in results['reviews']:
        dt = datetime.strptime(item['date'], '%B %d, %Y')
        isostr = dt.isoformat()  
        item['date'] = isostr

    # get sentiment for every review
    for item in results['reviews']:
        blob = TextBlob(item['snippet'])
        item['sentiment'] = sum([sentence.sentiment.polarity for sentence in blob.sentences]) / len(blob.sentences)

    return results