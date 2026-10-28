import nltk
from nltk.tokenize import word_tokenize
from nltk.text import Text

nltk.download("punkt")
nltk.download("punkt_tab")

text = """
Language models learn from language data.
Modern language models can generate fluent text.
The study of language models requires careful analysis of context.
Language data may come from many different domains.
"""

# Tokenize
tokens = word_tokenize(text)

# Normalize to lowercase
words = [token.lower() for token in tokens if token.isalpha()]

# Create an NLTK Text object
nltk_text = Text(words)

print("Concordance for 'language':")
nltk_text.concordance("language")

print("\nConcordance for 'models':")
nltk_text.concordance("models")