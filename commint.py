import tkinter as tk  # Import the tkinter module for GUI development.
from newspaper import Article  # Import the Article class from the newspaper library to fetch articles.
from textblob import TextBlob  # Import TextBlob to perform sentiment analysis on the article.
from googletrans import Translator  # Import the Translator class from googletrans library for translation.

# Function to summarize the article
def Summarize():
    url = urltext.get('1.0', "end-1c").strip()  # Get the URL input from the text box and remove leading/trailing spaces.

    article = Article(url)  # Create an Article object for the given URL.
    article.download()  # Download the article content.
    article.parse()  # Parse the article content to extract text, title, and metadata.
    article.nlp()  # Apply Natural Language Processing (NLP) to extract keywords and summary.

    # Enable editing in the GUI components (to update them with new content)
    title.config(state='normal')
    authors.config(state='normal')
    publish_date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')  # Clear the title text box.
    title.insert('1.0', translator.translate(article.title, src='auto', dest='am').text)  # Translate the article title to Amharic and insert it.

    authors.delete('1.0', 'end')  # Clear the authors text box.
    authors.insert('1.0', ", ".join(article.authors))  # Insert the authors' names as a comma-separated string.

    publish_date_text = article.publish_date if article.publish_date else "በግምት ቀን አልተሰጠም"  # Get the publication date or use a default message if it's not available.
    publish_date.delete('1.0', 'end')  # Clear the publish date text box.
    publish_date.insert('1.0', publish_date_text)  # Insert the publication date.

    summary.delete('1.0', 'end')  # Clear the summary text box.
    summary.insert('1.0', translator.translate(article.summary, src='auto', dest='am').text)  # Translate the article summary to Amharic and insert it.

    # Perform sentiment analysis on the article text using TextBlob
    analysis = TextBlob(article.text)  # Analyze the sentiment of the article text.
    sentiment_result = "አዎንታዊ" if analysis.polarity > 0 else "አሉታዊ" if analysis.polarity < 0 else "አልተለየም"  # Interpret the sentiment result and translate it to Amharic.

    sentiment.delete('1.0', 'end')  # Clear the sentiment analysis text box.
    sentiment.insert('1.0', f"እድሜ: {sentiment_result} (ነጥብ: {analysis.polarity})")  # Insert the sentiment result in Amharic along with the polarity score.

    # Disable editing in the GUI components after updating the text boxes with new content
    title.config(state='disabled')
    authors.config(state='disabled')
    publish_date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

# Create the GUI window
root = tk.Tk()  # Create a Tkinter root window for the application.
root.title('ዜና ማጠቃለያ')  # Set the title of the window in Amharic.
root.geometry("1200x600")  # Set the size of the window (1200x600 pixels).

# Title Label and Textbox
tlabel = tk.Label(root, text="ርዕስ")  # Create a label for the article title in Amharic.
tlabel.pack()  # Pack the label into the window.
title = tk.Text(root, height=1, width=140)  # Create a text box for displaying the title.
title.config(state='disabled', bg='#dddddd')  # Disable editing in the text box and set the background color.
title.pack()  # Pack the text box into the window.

# Authors Label and Textbox
alabel = tk.Label(root, text="ደራሲዎች")  # Create a label for the authors in Amharic.
alabel.pack()  # Pack the label into the window.
authors = tk.Text(root, height=1, width=140)  # Create a text box for displaying the authors.
authors.config(state='disabled', bg='#dddddd')  # Disable editing and set background color.
authors.pack()  # Pack the text box into the window.

# Publish Date Label and Textbox
plabel = tk.Label(root, text="የታተመበት ቀን")  # Create a label for the publish date in Amharic.
plabel.pack()  # Pack the label into the window.
publish_date = tk.Text(root, height=1, width=140)  # Create a text box for displaying the publish date.
publish_date.config(state='disabled', bg='#dddddd')  # Disable editing and set the background color.
publish_date.pack()  # Pack the text box into the window.

# Summary Label and Textbox
slabel = tk.Label(root, text="ማጠቃለያ")  # Create a label for the summary in Amharic.
slabel.pack()  # Pack the label into the window.
summary = tk.Text(root, height=20, width=140)  # Create a text box for displaying the summary.
summary.config(state='disabled', bg='#dddddd')  # Disable editing and set background color.
summary.pack()  # Pack the text box into the window.

# Sentiment Analysis Label and Textbox
selabel = tk.Label(root, text="የስሜት ትንተና")  # Create a label for the sentiment analysis in Amharic.
selabel.pack()  # Pack the label into the window.
sentiment = tk.Text(root, height=2, width=140)  # Create a text box for displaying sentiment analysis.
sentiment.config(state='disabled', bg='#dddddd')  # Disable editing and set background color.
sentiment.pack()  # Pack the text box into the window.

# URL Input Label and Textbox
urllabel = tk.Label(root, text="የጽሑፉን አድራሻ ያስገቡ")  # Create a label for the URL input in Amharic.
urllabel.pack()  # Pack the label into the window.
urltext = tk.Text(root, height=2, width=140)  # Create a text box for inputting the article URL.
urltext.pack()  # Pack the text box into the window.

# Summarize Button
btn = tk.Button(root, text="ማጠቃለያ", command=Summarize)  # Create a button for summarizing the article.
btn.pack()  # Pack the button into the window.

root.mainloop()  # Start the Tkinter event loop to display the GUI and handle user interactions.
