"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Part A: Find all area codes and mobile prefixes called by people in Bangalore
bangalore_calls = [call for call in calls if call[0].startswith('(080)')]
bangalore_called_numbers = [call[1] for call in bangalore_calls]
called_codes = set()

for number in bangalore_called_numbers:
    # Check for fixed line format
    match = re.search(r'\((\d+)\)', number)
    if match:
        called_codes.add("(" + match.group(1) + ")")
    # Check for mobile number format
    elif number[0] in ['7', '8', '9']:
        called_codes.add(number[:4])
    # Check for telemarketer format
    elif number.startswith('140'):
        called_codes.add('140')

print("The numbers called by people in Bangalore have codes:")
for code in sorted(list(called_codes)):
    print(code)

# Part B: Calculate percentage of calls from Bangalore to Bangalore
bangalore_to_bangalore_calls = [call for call in bangalore_calls if call[1].startswith('(080)')]
percentage = (len(bangalore_to_bangalore_calls) / len(bangalore_calls)) * 100

print("%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." % percentage)
