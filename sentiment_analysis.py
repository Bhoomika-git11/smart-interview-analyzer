from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# List of common filler words
filler_words = ['um', 'uh', 'like', 'actually', 'basically', 'you know', 'so', 'umm', 'i mean', 'well', 'right']

def count_filler_words(text):
    words = text.lower().split()
    return sum(1 for word in words if word in filler_words)

def classify_sentiment(compound , filler_count):
    if compound >= 0.5 and filler_count <=1:
        return "Positive"
    elif compound <= -0.2 or filler_count >= 3:
        return "Negative"
    else:
        return "Neutral"

def classify_emotion(compound, filler_count):
    if compound >= 0.6 and filler_count <=1:
        return "Confident"
    elif compound <= 0.0 or filler_count >= 3:
        return "Nervous"
    else:
        return "Neutral"

def analyze_sentiment_and_emotion(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    compound = sentiment_scores['compound']
    
    filler_count = count_filler_words(text)
    sentiment = classify_sentiment(compound , filler_count)
    emotion = classify_emotion(compound, filler_count)

    # Print for debugging/logging
    print("Transcript Text:", text)
    print(" Compound Score:", compound)
    print(" Filler Word Count:", filler_count)
    print("Sentiment:", sentiment)
    print(" Emotion:", emotion)

    return sentiment, compound, emotion, filler_count

