def rotated_array_search(input_list, number):
    """
    Find the index of a target number in a rotated sorted array using binary search.

    Args:
       input_list(array): The rotated sorted array to search in.
       number(int): The target number to find.
    Returns:
       int: The index of the target number if found, otherwise -1.
    """
    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        if input_list[mid] == number:
            return mid  # Target found at mid

        # Determine which half is sorted (left or right)
        if input_list[low] <= input_list[mid]:  # Left half is sorted
            if input_list[low] <= number < input_list[mid]:
                high = mid - 1  # Target is in the left half
            else:
                low = mid + 1  # Target is in the right half
        else:  # Right half is sorted
            if input_list[mid] < number <= input_list[high]:
                low = mid + 1  # Target is in the right half
            else:
                high = mid - 1  # Target is in the left half

    return -1  # Target not found


# Test cases
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])