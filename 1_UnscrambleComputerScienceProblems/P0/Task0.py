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

# The first record is at index 0
first_rec = texts[0]
# The last record is at index -1
last_rec = calls[-1]

# Print the first text record with the given format
print('First record of texts, %s texts %s at time %s' % (
    first_rec[0], first_rec[1], first_rec[2]))

# Print the last call record with the given format
print('Last record of calls, %s calls %s at time %s, lasting %s seconds' % (
    last_rec[0], last_rec[1], last_rec[2], last_rec[3]))