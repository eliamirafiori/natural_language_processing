import nltk
from nltk.tokenize import sent_tokenize

# Download the tokenizer model the first time
nltk.download("punkt")
nltk.download("punkt_tab")

text = """
Dr. Smith works at the University of Verona. He studies NLP.
The experiment used version 3.14. Was it successful? Yes, it was!
"""

sentences = sent_tokenize(text)

for i, sentence in enumerate(sentences, start=1):
    print(i, sentence)