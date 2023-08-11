def menu(**kwargs):
    """
    Take a dictionary with any number of keys; the values are all callables.
    If the user's input matches one of the keys, call the associated value.
    """
        
    user_msg = input("What would you like to search for? ").lower()
    
    if user_msg in kwargs.keys():
        return kwargs[user_msg]()
    
    return 'No results found'
