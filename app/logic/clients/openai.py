import openai
from models import Review
from app import db
from app.logic.commands.reviews import get_reviews
import app
openai.api_key = app.Config.OPENAI_API_KEY

def open_ai_summary(prompt, max_tokens=2408, temperature=0.49, top_p=1, frequency_penalty=0.2, presence_penalty=0):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty
    )
    return response.choices[0].text.strip()

def summarize_reviews(user, product_id, prompt):
    reviews = get_reviews(user, product_id)

    for review in reviews:
        prompt += review.snippet + "\n"

    return open_ai_summary(prompt)

def answer_reviews(reviews):
    # find all the reviews from the review.id
    review_ids = [review['id'] for review in reviews]
    reviews = Review.query.filter(Review.id.in_(review_ids)).all()

    for review in reviews:
        review_prompt = f"Answer the following review: {review.snippet}"
        review.answer = open_ai_summary(review_prompt)

        # update the review in the db
    
    db.session.commit()

    return reviews