import requests
import json
from textblob import TextBlob
from flask import Flask, jsonify

app = Flask(__name__)

# Function to fetch Bitcoin news
def get_bitcoin_news():
    news_api_url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=YOUR_API_KEY"
    response = requests.get(news_api_url)
    news_data = response.json()
    return news_data["articles"]

# Function to analyze sentiment
def analyze_sentiment():
    articles = get_bitcoin_news()
    sentiment_scores = []
    
    for article in articles:
        sentiment = TextBlob(article["title"]).sentiment.polarity
        sentiment_scores.append(sentiment)

    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)
    return round(avg_sentiment, 2)  # Normalize score (0 to 1)

# API Endpoint to send sentiment score
@app.route('/sentiment', methods=['GET'])
def send_sentiment():
    sentiment_score = analyze_sentiment()
    return jsonify({"sentiment_score": sentiment_score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)