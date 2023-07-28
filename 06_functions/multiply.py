def multiply(*nums):
    """Multiply any number of integers."""
    
    running_total = 1
    
    for num in nums:
        running_total *= num
    
    return running_total

