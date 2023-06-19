def sum_int(*args):
    """
    Takes an unspecified number/type of arguments, and adds together any 
    arguments that are integers
    """
    
    total = 0    
    for arg in args:
        if type(arg) == int: 
            total += arg
            
    return total

print(sum_int(33, 'hello', 'beautiful', 87, 'world'))