import tkinter as tk #graphic user interface
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





