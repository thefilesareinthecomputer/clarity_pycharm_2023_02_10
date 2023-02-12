# sentiment_analysis.py

import nltk
import random
import torch

nltk.download("vader_lexicon")
nltk.download("punkt")

from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

def generate_response(df, user_input: str) -> str:
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(user_input)
    sentiment_score = sentiment['compound']

    chatbot_responses = [
        "I'm glad to hear that!",
        "That's not very positive.",
        "I'm sorry to hear that.",
        "Can you tell me more about it?",
        "That sounds interesting."
    ]

    if sentiment_score > 0.5:
        return random.choice(chatbot_responses[:2])
    elif sentiment_score > -0.5 and sentiment_score <= 0.5:
        return random.choice(chatbot_responses[2:4])
    else:
        return random.choice(chatbot_responses[3:])
