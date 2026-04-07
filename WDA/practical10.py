import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon',quiet=True)

reviews = [
    "The product is amazing and works perfectly!",
    "Very disappointed with the quality.",
    "Customer service was okay, not great.",
    "Absolutely fantastic experience, highly recommend!",
    "Worst purchase ever. Waste of money.",
    "The item is decent for the price.",
    "I am extremely happy with this product",
    "Not bad, but could be better",
    "Terrible delivery experience",
    "Excellent quality and fast shipping"
]

df = pd.DataFrame({'Review': reviews})

sid = SentimentIntensityAnalyzer()

def get_sentiment(review):
    score = sid.polarity_scores(review)['compound']
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df['Review'].apply(get_sentiment)

print(df)

sentiment_counts = df['Sentiment'].value_counts()

plt.figure(figsize=(6,4))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis')
plt.title('Sentiment Analysis of Customer Reviews')
plt.xlabel('Sentiment')
plt.ylabel('Number of Reviews')
plt.show()

