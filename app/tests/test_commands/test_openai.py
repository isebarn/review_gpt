from app.logic.clients.openai import summarize_reviews
import pytest

@pytest.mark.skip
def test_summarize_reviews(review_objects):
    summary = summarize_reviews(review_objects)
    assert summary != ""
    assert len(summary) < 1000