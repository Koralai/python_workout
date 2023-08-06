def flip_dict(new_dict):
    """
    Take a dict and flip it (i.e., the original dict's keys become the
    new dict's values).
    """
    
    output = {}
    
    for key, val in new_dict.items():
        output[val] = key
        
    return output

my_dict = {
    'bilbo': 'hobbit',
    'galadriel': 'elf',
    'gandalf': 'wizard',
    'treebeard': 'ent',
}

print(flip_dict(my_dict))
