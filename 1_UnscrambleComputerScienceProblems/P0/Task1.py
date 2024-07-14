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


# Initialize an empty set to store unique telephone numbers
unique_numbers = set()

# Add all telephone numbers from texts to the set
for text in texts:
    unique_numbers.add(text[0])  # Add sending number
    unique_numbers.add(text[1])  # Add receiving number

# Add all telephone numbers from calls to the set
for call in calls:
    unique_numbers.add(call[0])  # Add calling number
    unique_numbers.add(call[1])  # Add receiving number

# Print the number of unique telephone numbers found
print('There are %s different telephone numbers in the records.' % len(unique_numbers))