import re

"""
Check https://www.w3schools.com/python/python_regex.asp
"""

text = """
On 14 March 2026, Dr. Smith sent 3 reports to the NLP Lab.
The meeting started at 10:30 and ended at 12:15.
For information, write to nlp-lab@example.org.
"""

# Dates
dates = re.findall(r"\b\d{1,2}\s+[A-Za-z]+\s+\d{4}\b", text)

# Times
times = re.findall(r"\b\d{1,2}:\d{2}\b", text)

# Integer numbers
integers = re.findall(r"\b\d+\b", text)

# Email addresses
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)

print("Dates:", dates)
print("Times:", times)
print("Integers:", integers)
print("Emails:", emails)

print("Number of dates:", len(dates))
print("Number of times:", len(times))
print("Number of integers:", len(integers))
print("Number of emails:", len(emails))
