import re
from collections import Counter
from nltk.corpus import stopwords

def extract_keywords(text, num_keywords=5):
    words = re.findall(r'\b\w{4,}\b', text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    top_keywords = Counter(filtered_words).most_common(num_keywords)
    return [word for word, _ in top_keywords]