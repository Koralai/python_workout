def get_highest_vals(dict_name):
    """
    Takes in a dictionary. Sorts the data by highest value, and returns the 
    sorted data as a list of tuples (each containing a key and its value).
    """
    
    # sort the dict by value 
    # sorted() will return a list of keys in the order we want, but with no vals
    keys_sorted_by_vals = sorted(dict_name, key=dict_name.get, reverse=True)
    
    # reassociate the vals with the sorted keys
    sorted_data = []    
    for key in keys_sorted_by_vals:
        sorted_data.append((key, dict_name.get(key)))
    
    return sorted_data
