import openai
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