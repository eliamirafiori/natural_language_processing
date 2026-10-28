import nltk
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

nltk.download("punkt")
nltk.download("punkt_tab")

text = """
Natural language processing is an important field of artificial intelligence.
Many natural language processing systems analyse large text collections.
Machine learning methods are widely used in natural language processing.
Artificial intelligence applications often rely on machine learning.
"""

# Tokenize, lowercase, keep only alphabetic tokens
tokens = word_tokenize(text)
words = [token.lower() for token in tokens if token.isalpha()]

# Create the bigram finder
finder = BigramCollocationFinder.from_words(words)

# Association measures
measures = BigramAssocMeasures()

# Most frequent bigrams
print("Most frequent bigrams:")
for bigram, frequency in finder.ngram_fd.most_common(10):
    print(bigram, frequency)

# Best bigrams according to PMI
print("\nBest collocations according to PMI:")
for bigram in finder.nbest(measures.pmi, 10):
    print(bigram)
