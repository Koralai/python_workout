def count_items(*items):
    """Counts the items in a series"""
    
    new_list = []    
    for item in items:
        new_list.append(item)
        
    return len(new_list)
    
def myaverage(*numbers):
    """Takes a series of numbers of any length and returns the average"""
    
    avg_numerator = 0    
    for number in numbers:
        avg_numerator += number
    
    avg_denominator = count_items(*numbers)
    
    return (avg_numerator / avg_denominator)


print(myaverage(83, 88, 87, 86))