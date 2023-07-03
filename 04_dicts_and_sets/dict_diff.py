def dict_diff(dict_1, dict_2):
    """Compare two dictionaries and return the differences between them"""
    
    output = {}
    
    # collect all unique keys in a set (using union operator)
    all_keys = dict_1.keys() | dict_2.keys()
    
    for key in all_keys:
        if dict_1.get(key) != dict_2.get(key):
            output[key] = [dict_1.get(key), dict_2.get(key)]
    
    return output
    
frodo = {
    'first_n': 'frodo',
    'last_n': 'baggins',
    'age': 50,
    'protagonist_of': 'The Lord of the Rings',
    'best_friend': 'sam',
}

bilbo = {
    'first_n': 'bilbo',
    'last_n': 'baggins',
    'age': 111,
    'protagonist_of': 'The Hobbit',
}

print(dict_diff(frodo, bilbo))
