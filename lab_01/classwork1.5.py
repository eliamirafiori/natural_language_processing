import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download("punkt")
nltk.download("punkt_tab")

text = """
The researchers connected several systems.
They are connecting new components and testing the connections.
The studies also considered different processing strategies.
"""

# Tokenization
tokens = word_tokenize(text)

# Porter stemmer
stemmer = PorterStemmer()

# Keep only alphabetic tokens
words = [token for token in tokens if token.isalpha()]

# Stem each word
for word in words:
    stem = stemmer.stem(word.lower())
    print(f"{word:15} -> {stem}")