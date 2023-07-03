def dict_diff(dict_1, dict_2):
    """Compare two dictionaries and return the differences between them"""
    
    output = {}
    
    # collect all unique keys in a set (using union operator)
    all_keys = dict_1.keys() | dict_2.keys()
    
    # if values are different, record both values as a list in the output dict
    for key in all_keys:
        
        if key in dict_1 and key in dict_2:
            if dict_1[key] == dict_2[key]:
                continue
            output[key] = [dict_1[key], dict_2[key]]
            
        elif key in dict_1:
            output[key] = [dict_1[key], None]
        else:
            output[key] = [None, dict_2[key]]
    
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
