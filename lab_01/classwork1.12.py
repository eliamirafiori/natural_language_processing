from collections import Counter
from nltk.util import ngrams

text = """
the cat sat on the mat
the cat ate the fish
the dog sat on the mat
"""

words = text.lower().split()

# Vocabulary
vocabulary = set(words)
V = len(vocabulary)

# Counts
unigram_counts = Counter(words)
bigram_counts = Counter(ngrams(words, 2))

def mle_bigram_probability(previous_word, current_word):
    return (
        bigram_counts[(previous_word, current_word)]
        / unigram_counts[previous_word]
    )

def laplace_bigram_probability(previous_word, current_word):
    return (
        bigram_counts[(previous_word, current_word)] + 1
    ) / (
        unigram_counts[previous_word] + V
    )

pairs = [
    ("the", "cat"),
    ("the", "dog"),
    ("the", "mat"),
    ("the", "mouse")
]

print("Vocabulary size:", V)

for previous_word, current_word in pairs:

    mle = mle_bigram_probability(previous_word, current_word)

    laplace = laplace_bigram_probability(
        previous_word,
        current_word
    )

    print(
        f"P({current_word} | {previous_word}) "
        f"MLE = {mle:.3f}   "
        f"Laplace = {laplace:.3f}"
    )