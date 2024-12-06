import tkinter as tk #graphic user interface

import analysis
import nltk #for natural language processor
from textblob import TextBlob #for tenement analysis

from newspaper import Article
nltk.download('punkt_tab')


#sumerazation and sentiment analysis

url = 'https://www.britannica.com/biography/Abiy-Ahmed'

article = Article(url)


article.download()
article.parse()

article.nlp()


print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publish Date: {article.publish_date}')
print(f'Summary: {article.summary}')




#from now on we gonna built a user graphic page
# the next part is to analysis the article meaning the article might be positive or negative and tell me


analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'sentiment: {"positive" if analysis.polarity > 0 else"negative" if analysis.polarity <0 else "natural"}')

