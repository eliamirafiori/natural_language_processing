import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter

nltk.download("punkt")
nltk.download("punkt_tab")

text = """
The language model predicts the next word.
The model learns patterns from language data.
The next word depends on the previous words.
"""

# Tokenize, lowercase, keep only alphabetic tokens
tokens = word_tokenize(text)
words = [token.lower() for token in tokens if token.isalpha()]

# Generate n-grams
unigrams = list(ngrams(words, 1))
bigrams = list(ngrams(words, 2))
trigrams = list(ngrams(words, 3))

print("First 10 bigrams:")
for bg in bigrams[:10]:
    print(bg)

print("\nFirst 10 trigrams:")
for tg in trigrams[:10]:
    print(tg)

# Count distinct n-grams
print("\nNumber of unigrams:", len(unigrams))
print("Distinct unigrams:", len(set(unigrams)))

print("Number of bigrams:", len(bigrams))
print("Distinct bigrams:", len(set(bigrams)))

print("Number of trigrams:", len(trigrams))
print("Distinct trigrams:", len(set(trigrams)))

# Find repeated n-grams
bigram_counts = Counter(bigrams)
trigram_counts = Counter(trigrams)

print("\nRepeated bigrams:")
for bg, count in bigram_counts.items():
    if count > 1:
        print(bg, count)

print("\nRepeated trigrams:")
for tg, count in trigram_counts.items():
    if count > 1:
        print(tg, count)