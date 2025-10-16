import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import re
from pymorphy3 import MorphAnalyzer
from functools import lru_cache
import pandas as pd

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

morph = MorphAnalyzer()

@lru_cache(maxsize=10000)
def lemmatize_word(word):
    return morph.parse(word)[0].normal_form

def preprocess_text(text):
    if pd.isna(text):
        return ""
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.replace('«', ' ').replace('»', ' ')
    text = text.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
    tokens = text.split()
    tokens = [token.replace('-', ' ') for token in tokens]
    tokens = [word for sublist in [word_tokenize(t, language='russian') for t in tokens] for word in sublist]
    stop_words = set(stopwords.words('russian'))
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [lemmatize_word(word) for word in tokens]
    return ' '.join(tokens)