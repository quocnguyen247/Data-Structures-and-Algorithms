"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

outgoing_calls = set(call[0] for call in calls)  # O(n)
outgoing_texts = set(text[0] for text in texts)  # O(n)
incoming_calls = set(call[1] for call in calls)  # O(n)
incoming_texts = set(text[1] for text in texts)  # O(n)

possible_telemarketers = outgoing_calls - outgoing_texts - incoming_calls - incoming_texts

print("These numbers could be telemarketers:")
for telemarketer in sorted(possible_telemarketers):  # O(n log n)
    print(telemarketer)