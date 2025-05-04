import re
from wordcloud import STOPWORDS, WordCloud
from collections import Counter
import matplotlib.pyplot as plt

## Step 1: Data Collection
text_data = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book"

## Step 2: Text Pre-processing

# Tokenisation: Split text into words
words = text_data.split()

# Lowercasing: Convert words to lowercase
words = [word.lower() for word in words]

# Removing Punctuation and Symbols
words = [re.sub(r"[^\w\s]", "", word) for word in words]

# Stop Word Removal
stop_words = set(STOPWORDS)
words = [word for word in words if word not in stop_words]

## Step 3: Word Frequency Calculation
word_counts = Counter(words)

## Step 4: Generate the Word Cloud

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color="white")

# Generate the word cloud
wordcloud.generate_from_frequencies(word_counts)

# Display the word cloud using Matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
