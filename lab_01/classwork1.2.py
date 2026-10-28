import re

text = """
Prof. Brown met Dr. Green on 3/9/2026.
The next meeting is scheduled for 03-10-2026 at 9:00.
Contact john.smith@univr.it or support-team@example.com.
The experiment obtained scores of 91.5%, 87%, and 0.93.
Version 3.14 of the software was released yesterday.
"""

# Dates: 3/9/2026 or 03-10-2026
dates = re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b", text)

# Email addresses
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)

# Percentages: integer or decimal number followed by %
percentages = re.findall(r"\b\d+(?:\.\d+)?%", text)

# Decimal numbers
decimals = re.findall(r"\b\d+\.\d+\b", text)

print("Dates:", dates)
print("Emails:", emails)
print("Percentages:", percentages)
print("Decimal numbers:", decimals)