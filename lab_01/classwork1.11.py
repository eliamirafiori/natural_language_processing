from collections import Counter
from nltk.util import ngrams

text = """
the cat sat on the mat
the cat ate the fish
the dog sat on the mat
"""

# Simple tokenization
words = text.lower().split()

# Count unigrams
unigram_counts = Counter(words)

# Generate and count bigrams
bigrams = list(ngrams(words, 2))
bigram_counts = Counter(bigrams)

def bigram_probability(previous_word, current_word):
    numerator = bigram_counts[(previous_word, current_word)]
    denominator = unigram_counts[previous_word]

    if denominator == 0:
        return 0

    return numerator / denominator

pairs = [
    ("the", "cat"),
    ("the", "dog"),
    ("cat", "sat"),
    ("cat", "ate"),
    ("the", "mat"),
    ("the", "mouse")
]

for previous_word, current_word in pairs:
    p = bigram_probability(previous_word, current_word)
    print(f"P({current_word} | {previous_word}) = {p:.3f}")