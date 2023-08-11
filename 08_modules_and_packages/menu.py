def menu(**options):
    """
    Take a dictionary with any number of keys; the values are all callables.
    If the user's input matches one of the keys, call the associated value.
    """
    option_string = ' / '.join(sorted(options))    
    user_msg = input(f"Enter an option: {option_string} ").lower()
    
    if user_msg in options:
        return options[user_msg]()
    
    return 'No results found'
