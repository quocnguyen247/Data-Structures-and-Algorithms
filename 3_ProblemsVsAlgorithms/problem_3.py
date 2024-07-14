def rearrange_digits(input_list):
    """
    Rearrange Array Elements to form two numbers such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int, int): Two numbers with maximum sum
    """
    # Frequency array for digits 0-9
    freq = [0] * 10
    for digit in input_list:
        freq[digit] += 1
    
    # Construct numbers
    num1 = []
    num2 = []
    
    # Build numbers by alternating digits of highest value
    toggle = True
    for digit in range(9, -1, -1):
        while freq[digit] > 0:
            if toggle:
                num1.append(digit)
            else:
                num2.append(digit)
            freq[digit] -= 1
            toggle = not toggle
    
    # Convert lists of digits to integers
    num1 = int(''.join(map(str, num1)))
    num2 = int(''.join(map(str, num2)))
    
    return (num1, num2)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])