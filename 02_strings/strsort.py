def sort_string(string):
    """
    Accept a string and return a string containing the same characters, 
    sorted from lowest to highest Unicode value
    """

    unicode_vals = []
    output = ''
    
    for char in string:
        unicode_val = ord(char)
        unicode_vals.append(unicode_val)
    
    unicode_vals.sort()

    for val in unicode_vals:
        char = chr(val)
        output += char
    
    return output    
