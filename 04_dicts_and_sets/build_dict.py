def build_dict(*args):
    """
    Take any even number of arguments and build a dictionary from them.
    Even-indexed args are keys, and odd-indexed args are values.
    """

    output = {}
    i = 0

    for _ in args:
        if i < len(args):
            new_key = args[i]
            new_value = args[i+1]
            output[new_key] = new_value
            i += 2    
    
    return output

print(build_dict('first', 'frodo', 'last', 'baggins', 'age', 50))
