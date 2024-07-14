def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return None  # Return None for empty list
    
    # Initialize min and max with the first element
    min_val = max_val = ints[0]
    
    # Single traversal to find min and max
    for num in ints[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    
    return (min_val, max_val)

# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Additional test cases
print("Pass" if ((0, 9) == get_min_max([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) else "Fail")
print("Pass" if ((0, 9) == get_min_max([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) else "Fail")
print("Pass" if ((0, 1) == get_min_max([0, 1])) else "Fail")
print("Pass" if ((5, 5) == get_min_max([5])) else "Fail")
print("Pass" if (None == get_min_max([])) else "Fail")