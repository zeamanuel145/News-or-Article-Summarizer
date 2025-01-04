import tkinter as tk
from newspaper import Article
from textblob import TextBlob
from deep_translator import GoogleTranslator

# Function to summarize the article
def Summarize():
    url = urltext.get('1.0', "end-1c").strip()

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # Create a Translator object
    translator = GoogleTranslator(source='auto', target='am')

    # Summarize and translate to Amharic
    title.config(state='normal')
    authors.config(state='normal')
    publish_date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', translator.translate(article.title))

    authors.delete('1.0', 'end')
    authors.insert('1.0', ", ".join(article.authors))

    publish_date_text = article.publish_date if article.publish_date else "በግምት ቀን አልተሰጠም"
    publish_date.delete('1.0', 'end')
    publish_date.insert('1.0', publish_date_text)

    summary.delete('1.0', 'end')
    summary.insert('1.0', translator.translate(article.summary))

    # Sentiment analysis and translation to Amharic
    analysis = TextBlob(article.text)
    sentiment_result = "አዎንታዊ" if analysis.polarity > 0 else "አሉታዊ" if analysis.polarity < 0 else "አልተለየም"

    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f"እድሜ: {sentiment_result} (ነጥብ: {analysis.polarity})")

    title.config(state='disabled')
    authors.config(state='disabled')
    publish_date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


# Create the GUI
root = tk.Tk()
root.title('ዜና ማጠቃለያ')
root.geometry("1200x600")

# Title Label and Textbox
tlabel = tk.Label(root, text="ርዕስ")
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

# Authors Label and Textbox
alabel = tk.Label(root, text="ደራሲዎች")
alabel.pack()
authors = tk.Text(root, height=1, width=140)
authors.config(state='disabled', bg='#dddddd')
authors.pack()

# Publish Date Label and Textbox
plabel = tk.Label(root, text="የታተመበት ቀን")
plabel.pack()
publish_date = tk.Text(root, height=1, width=140)
publish_date.config(state='disabled', bg='#dddddd')
publish_date.pack()

# Summary Label and Textbox
slabel = tk.Label(root, text="ማጠቃለያ")
slabel.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

# Sentiment Analysis Label and Textbox
selabel = tk.Label(root, text="የስሜት ትንተና")
selabel.pack()
sentiment = tk.Text(root, height=2, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

# URL Input Label and Textbox
urllabel = tk.Label(root, text="የጽሑፉን አድራሻ ያስገቡ")
urllabel.pack()
urltext = tk.Text(root, height=2, width=140)
urltext.pack()

# Summarize Button
btn = tk.Button(root, text="ማጠቃለያ", command=Summarize)
btn.pack()

root.mainloop()
