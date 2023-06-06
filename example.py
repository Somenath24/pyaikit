import os

from authentication import Authenticator
from sentiment_analysis.sentiment_analyzer import sentiment_analyzer
from text_summerization.text_summerizer import text_summerizer
auth = Authenticator()

# Set up authentication with the API key
api_key = 'YOUR_API_KEY'
org_id = 'YOUR_org_id'
openai1=auth.setup(api_key,org_id)

#Sentiment analysis
obj=sentiment_analyzer()
obj.generate_sentiment_score(openai1,"text")
obj.generate_advanced_sentiment(openai1,"text")

#text summerizer
obj=text_summerizer()
obj.summarize_pdf(openai1, no_of_words="no of words in per page summary", file_path="pdf file path", start_page="start page number", end_page="end page number")