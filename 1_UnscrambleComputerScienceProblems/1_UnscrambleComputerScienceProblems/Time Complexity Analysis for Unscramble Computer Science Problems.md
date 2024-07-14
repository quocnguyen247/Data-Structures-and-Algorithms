# Run time analysis
This file explains the n time analysis (Worst Case Big O Notation) for each solution they produced. 
Analysis will leave apart the load of the current files.

## Task0
File Reading: (O(n + m)), where (n) is the number of lines in texts.csv and (m) is the number of lines in calls.csv.
Accessing Records: (O(1))
Printing Records: (O(1))

## Task1
Reading Files: (O(n + m))
Processing Text Records: (O(n))
Processing Call Records: (O(m))
Adding to Set: (O(n + m))
Printing Result: (O(1))

Therefore, the overall time complexity of the code is: (O(n + m))

## Task2
Reading Files: (O(n + m))
Processing Call Records: (O(n))
Finding Maximum Duration: (O(n))
Printing Result: (O(1))

Therefore, the total time complexity of the code is: (O(n + m))

## Task3
Reading Files: (O(n + m))
Filtering Bangalore Calls: (O(m))
Extracting Called Numbers: (O(k))
Finding Area Codes and Prefixes: (O(k))
Sorting Codes: (O(c \log c))

Thus, combining these operations, the overall time complexity of the code is: (O(n + m + k \log k))

## Task4
Reading Files: (O(n + m))
Extracting Unique Phone Numbers: (O(n + m))
Finding Possible Telemarketers: (O(n + m))
Sorting Possible Telemarketers: (O(k \log k))

The sorting operation dominates the overall time complexity. Thus, considering all operations, the total time complexity of the code is: (O(n + m + k \log k))