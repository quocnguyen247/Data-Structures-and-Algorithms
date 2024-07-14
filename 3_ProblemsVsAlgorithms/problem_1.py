def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored square root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number")
    
    if number == 0:
        return 0
    
    low, high = 0, number
    
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid
        
        if mid_squared == number:
            return mid
        elif mid_squared < number:
            low = mid + 1
        else:
            high = mid - 1
    
    return high

# Test cases
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")