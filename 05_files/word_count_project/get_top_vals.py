def get_top_vals(dict_name, num_x):
    """
    Takes in a dictionary (which has numbers for values) and a number, x.
    Returns the highest [x] number of values (e.g., the top 10 highest).
    """
    
    # sort the dict by value 
    # sorted() will return a list of keys in the order we want, but with no vals
    keys_sorted_by_vals = sorted(dict_name, key=dict_name.get, reverse=True)
    
    # reassociate the vals with the sorted keys
    sorted_data = []
    
    i = 1
    for key in keys_sorted_by_vals:
        if i <= num_x:
            sorted_data.append((key, dict_name.get(key)))
            i += 1
    
    return sorted_data
