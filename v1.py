# # Function to summarize the article
# def Summarize():
#     url = urltext.get('1.0', "end-1c").strip()  # Get the URL and strip any trailing newlines
#
#     article = Article(url)
#     article.download()
#     article.parse()
#     article.nlp()
#
#     # Update UI elements with article details
#     title.config(state='normal')
#     authors.config(state='normal')
#     publish_date.config(state='normal')
#     summary.config(state='normal')
#     sentiment.config(state='normal')
#
#     title.delete('1.0', 'end')
#     title.insert('1.0', article.title)
#
#     authors.delete('1.0', 'end')
#     authors.insert('1.0', ", ".join(article.authors))
#
#     # Check if publish_date is None and handle it accordingly
#     publish_date_text = article.publish_date if article.publish_date else "N/A"
#     publish_date.delete('1.0', 'end')
#     publish_date.insert('1.0', publish_date_text)
#
#     summary.delete('1.0', 'end')
#     summary.insert('1.0', article.summary)
#
#     # Sentiment analysis
#     analysis = TextBlob(article.text)
#     sentiment_result = "positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"
#
#     sentiment.delete('1.0', 'end')
#     sentiment.insert('1.0', f"Sentiment: {sentiment_result} (Polarity: {analysis.polarity})")
#
#     # Disable text fields again after update
#     title.config(state='disabled')
#     authors.config(state='disabled')
#     publish_date.config(state='disabled')
#     summary.config(state='disabled')
#     sentiment.config(state='disabled')
#
#
# # Create the GUI
# root = tk.Tk()
# root.title('News Summarizer')
# root.geometry("1200x600")
#
# # Title Label and Textbox
# tlabel = tk.Label(root, text="Title")
# tlabel.pack()
# title = tk.Text(root, height=1, width=140)
# title.config(state='disabled', bg='#dddddd')
# title.pack()
#
# # Authors Label and Textbox
# alabel = tk.Label(root, text="Authors")
# alabel.pack()
# authors = tk.Text(root, height=1, width=140)
# authors.config(state='disabled', bg='#dddddd')
# authors.pack()
#
# # Publish Date Label and Textbox
# plabel = tk.Label(root, text="Publish Date")
# plabel.pack()
# publish_date = tk.Text(root, height=1, width=140)
# publish_date.config(state='disabled', bg='#dddddd')
# publish_date.pack()
#
# # Summary Label and Textbox
# slabel = tk.Label(root, text="Summary")
# slabel.pack()
# summary = tk.Text(root, height=20, width=140)
# summary.config(state='disabled', bg='#dddddd')
# summary.pack()
#
# # Sentiment Analysis Label and Textbox
# selabel = tk.Label(root, text="Sentiment Analysis")
# selabel.pack()
# sentiment = tk.Text(root, height=2, width=140)
# sentiment.config(state='disabled', bg='#dddddd')
# sentiment.pack()
#
# # URL Input Label and Textbox
# urllabel = tk.Label(root, text="Enter Article URL")
# urllabel.pack()
# urltext = tk.Text(root, height=2, width=140)
# urltext.pack()
#
# # Summarize Button
# btn = tk.Button(root, text="Summarize", command=Summarize)
# btn.pack()
#
# root.mainloop()



##########################################



#
# import tkinter as tk #graphic user interface
#  from lxml.doctestcompare import strip
# # from newspaper.nlp import summarize
# # from textblob import TextBlob #for tenement analysis
# #
# # from newspaper import Article
# #
# # #we need to create the function button , when we click the button we want to Summarize the article
# # def Summarize():
# #     url = urltext.get('1.0', "end-1c").strip()  # Get the URL and strip any trailing newlines
# #
# #     article = Article(url)
# #     article.download()
# #     article.parse()
# #     article.nlp()
# #
# #     # Update UI elements with article details
# #     title.config(state='normal')
# #     authors.config(state='normal')
# #     publish_date.config(state='normal')
# #     summary.config(state='normal')
# #     sentiment.config(state='normal')
# #
# #     title.delete('1.0', 'end')
# #     title.insert('1.0', article.title)
# #
# #     authors.delete('1.0', 'end')
# #     authors.insert('1.0', ", ".join(article.authors))
# #
# #     publish_date.delete('1.0', 'end')
# #     publish_date.insert('1.0', article.publish_date)
# #
# #     summary.delete('1.0', 'end')
# #     summary.insert('1.0', article.summary)
# #
# #     # Sentiment analysis
# #     analysis = TextBlob(article.text)
# #     sentiment_result = "positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"
# #
# #     sentiment.delete('1.0', 'end')
# #     sentiment.insert('1.0', f"Sentiment: {sentiment_result} (Polarity: {analysis.polarity})")
# #
# #     # Disable text fields again after update
# #     title.config(state='disabled')
# #     authors.config(state='disabled')
# #     publish_date.config(state='disabled')
#      summary.config(state='disabled')
#      sentiment.config(state='disabled')
#
#
#
#
#
#          #the next part is to analysis the article meaning the article might be positive or negative and tell me
#          #from now on we gonna built a user graphic page
#
# root = tk.Tk()
# root.title('News Summarizer')
# root.geometry("1200x600")#it is to tell us how much the height and the wight really is.
#
#
#          #now we gonna built individual buttons,labels and add them to the root
# tlabel =tk.Label(root, text="Title")
# tlabel.pack()
#          #now the box for the title
# title = tk.Label(root, height=1, width=140)
# title.config(state='disabled', bg='#dddddd')#we don't want the user to put the title expect fot the url
# title.pack()
# #
# alabel =tk.Label(root, text="Authors")
# alabel.pack()
# #
# authors = tk.Label(root, height=1, width=140)
# authors.config(state='disabled', bg='#dddddd')#we don't want the user to put the title expect fot the url
# authors.pack()
# #
# #
# #
# plabel =tk.Label(root, text="Publish Date")
# plabel.pack()
# #
# publish_date = tk.Label(root, height=1, width=140)
# publish_date.config(state='disabled', bg='#dddddd')#we don't want the user to put the title expect fot the url
# publish_date.pack()
# #
# #
# slabel =tk.Label(root, text="Summary")
# slabel.pack()
# #
# #summary = tk.Label(root, height=20, width=140)
# summary.config(state='disabled', bg='#dddddd')#we don't want the user to put the title expect fot the url
# summary.pack()
# #
# #
# selabel =tk.Label(root, text="sentiment analysis")
# selabel.pack()
# #
# sentiment = tk.Label(root, height=2, width=140)
# sentiment.config(state='disabled', bg='#dddddd')#we don't want the user to put the title expect fot the url
# sentiment.pack()
# #
# urllabel =tk.Label(root, text="sentiment analysis")
# urllabel.pack()
# #
# urltext = tk.Label(root, height=2, width=140)
# urltext.pack()
# #
#          #button
# btn =tk.Button(root, text="Summarize", command= summarize)
# btn.pack()
#
# root.mainloop()