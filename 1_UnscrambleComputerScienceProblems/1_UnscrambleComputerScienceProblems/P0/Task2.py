"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Initialize a dictionary to keep track of total call duration per phone number
calls_duration = {}

# Populate the dictionary with call durations for each number
for call in calls:
    caller, receiver, _, duration = call
    # Convert duration to integer for summing
    duration = int(duration)

    # Update the caller's total call duration
    if caller in calls_duration:
        calls_duration[caller] += duration
    else:
        calls_duration[caller] = duration

    # Update the receiver's total call duration (since receiving a call also counts as time on the phone)
    if receiver in calls_duration:
        calls_duration[receiver] += duration
    else:
        calls_duration[receiver] = duration

# Find the phone number with the longest total call duration
longest_call_number, longest_call_duration = max(calls_duration.items(), key=lambda item: item[1])

# Print the result
print('%s spent the longest time, %s seconds, on the phone during September 2016.' % (longest_call_number, longest_call_duration))

