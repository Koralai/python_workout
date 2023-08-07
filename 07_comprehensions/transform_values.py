def transform_values(function, dictionary):
    """
    Apply a function to each value of a dictionary.
    """
    return {key: function(val) 
            for key, val in dictionary.items()}

def get_square(number):
    """Return the square of a number."""
    return number * number

new_dict = {'a': 1, 'b': 2, 'c': 3,}
    
print(transform_values(get_square, new_dict))
