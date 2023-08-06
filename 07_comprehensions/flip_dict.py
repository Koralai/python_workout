def flip_dict(new_dict):
    """
    Take a dict and flip it (i.e., the original dict's keys become the
    new dict's values).
    """
    return {val:key
              for key, val in new_dict.items()}

my_dict = {
    'bilbo': 'hobbit',
    'galadriel': 'elf',
    'gandalf': 'wizard',
    'treebeard': 'ent',
}

print(flip_dict(my_dict))
