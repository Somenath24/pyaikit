#pip install pyaikit
import os

from pyaikit import authentication, sentiment_analysis,text_summerization
from pyaikit.authentication import Authenticator
from pyaikit.sentiment_analysis.sentiment_analyzer import sentiment_analyzer
from pyaikit.text_summerization.text_summerizer import text_summerizer
from pyaikit.text_generation.text_generator import text_generator
from pyaikit.translation.translator import translator

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


#text generator
obj=text_generator()
obj.generate_text(openai1, topic="title of your blog", no_of_words="20")


#text generator
obj=translator()
obj.translate_text(openai1, text="text", language="Bengali")