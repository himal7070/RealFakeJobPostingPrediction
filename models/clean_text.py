

import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

def clean_text(text):
    if text is None:
        return ""
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove instances of 're:', dashes, and underscores
    text = re.sub(r're:', '', text)
    text = re.sub(r'[-_]', '', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www.\S+', '', text)
    
    # Remove email addresses
    text = re.sub(r'\S*@\S*\s?', '', text)
    
    # Remove text within square brackets
    text = re.sub(r'\[[^]]]*\]', '', text)
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Replace newlines with spaces
    text = re.sub(r'\n', ' ', text)
    
    # Normalize contractions
    contractions = {
        r"\'ve": " have",
        r"can't": " cannot",
        r"n't": " not",
        r"I'm": "I am",
        r" m ": " am ",
        r"\'re": " are",
        r"\'d": " would",
        r"\'ll": " will"
    }
    for contraction, replacement in contractions.items():
        text = re.sub(contraction, replacement, text)
    
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # Tokenize the text
    tokens = text.split()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Stem the filtered tokens using PorterStemmer
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    
    # Join stemmed tokens back into a single string
    processed_text = ' '.join(stemmed_tokens)
    
    return processed_text
