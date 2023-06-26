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

def sort_string_2(string):
    """A more concise version of the sort_string function"""
    sorted_chrs = sorted(string) # sorts the chars, but returns a list
    
    return ''.join(sorted_chrs)
