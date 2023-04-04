from app.logic.clients.serpapi import search_product
from app.logic.clients.serpapi import get_reviews
import pytest

def test_serpapi_get_reviews():
    reviews = get_reviews("com.google.android.youtube")
    assert reviews.get('reviews')

def test_serpapi_search_product():
    results = search_product("youtube")
    assert results.get('organic_results')


""" WRITE TESTS WRITE TESTS WRITE 

EVERYTHING IS TESTSS """