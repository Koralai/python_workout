def mysum(*numbers):
    """Takes a series of numbers of any length and adds them together"""
    
    total = 0
    
    for number in numbers:
        total += number
    
    return total

print(mysum(2,15,82,99,12))