import nltk
from nltk.tokenize import word_tokenize
from nltk import FreqDist

nltk.download("punkt")
nltk.download("punkt_tab")

text = """
Natural language processing studies language with computational methods.
Language models learn patterns from language data.
Computational models can reveal frequent words and recurring structures.
"""

# Tokenize
tokens = word_tokenize(text)

# Normalize: lowercase and keep alphabetic tokens only
words = [token.lower() for token in tokens if token.isalpha()]

# Frequency distribution
freq = FreqDist(words)

print("10 most frequent words:")
print(freq.most_common(10))

print("\nSelected frequencies:")
print("language:", freq["language"])
print("models:", freq["models"])
print("computational:", freq["computational"])

print("\nNumber of tokens:", len(words))
print("Number of types:", len(set(words)))