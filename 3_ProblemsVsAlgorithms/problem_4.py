def sort_012(input_list):
    """
    Given an input array consisting only of 0, 1, and 2, sort the array in a single traversal.
    
    Args:
       input_list(list): List to be sorted
    """
    low, mid, high = 0, 0, len(input_list) - 1
    
    while mid <= high:
        if input_list[mid] == 0:
            # Swap 0 to the front
            input_list[low], input_list[mid] = input_list[mid], input_list[low]
            low += 1
            mid += 1
        elif input_list[mid] == 1:
            # 1 is in the correct place
            mid += 1
        else:
            # Swap 2 to the end
            input_list[high], input_list[mid] = input_list[mid], input_list[high]
            high -= 1
    
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])