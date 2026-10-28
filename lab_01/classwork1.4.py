import nltk
from nltk.tokenize import word_tokenize

# Download the tokenizer model the first time
nltk.download("punkt")
nltk.download("punkt_tab")

text = """
Dr. Smith can't attend today's NLP meeting.
The state-of-the-art system achieved 97.5%.
Visit https://www.example.org for details.
"""

tokens = word_tokenize(text)

for token in tokens:
    print(token)