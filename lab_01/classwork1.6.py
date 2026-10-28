import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")
nltk.download("omw-1.4")

text = """
The children were running through the fields.
Some mice had eaten the food, while the better trained dogs were watching them.
"""

tokens = word_tokenize(text)

lemmatizer = WordNetLemmatizer()

print("Without POS information:")
for token in tokens:
    if token.isalpha():
        lemma = lemmatizer.lemmatize(token.lower())
        print(f"{token:12} -> {lemma}")