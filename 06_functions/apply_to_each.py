def apply_to_each(funct, iterable):
    """
    Take a function (that takes a single argument) and an iterable. 
    Apply to function to each item in the iterable.
    """
    output = []
    
    for item in iterable:
        output.append(funct(item))
        
    return output

def multiply_by_6(num):
    return num * 6

numbers = [1,2,3,4,5]

print(apply_to_each(multiply_by_6, numbers))
