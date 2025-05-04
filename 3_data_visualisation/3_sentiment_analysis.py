from textblob import TextBlob
import matplotlib.pyplot as plt

# Sample sentences
sentences = [
    "I love this product!",
    "This service is terrible.",
    "I'm not sure if I like this.",
    "This is the best experience ever.",
    "This is bad.",
]

# Sentiment analysis
sentiments = [TextBlob(sentence).sentiment.polarity for sentence in sentences]

# Visualisation
plt.figure(figsize=(10, 6))
plt.plot(sentiments, marker="o", linestyle="-", color="b")
plt.title("Sentiment Analysis of Sample Sentences")
plt.xlabel("Sentence Index")
plt.ylabel("Sentiment Polarity")
plt.xticks(range(len(sentences)))
plt.axhline(0, color="red", linestyle="--")  # Line at polarity=0 for reference
plt.ylim(-1, 1)
plt.grid(True)
plt.show()
