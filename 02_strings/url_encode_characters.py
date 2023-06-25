"""
Convert a string to URL encoding. Find characters that aren't letters or numbers 
and replace them with '%' plus the character's ASCII value in hexadecimal
"""

def get_url_encoding(string):
    output = ''
    printable_chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    
    for char in string:        
        if char.lower() not in printable_chars:
            ascii_val = ord(char)
            hex_val = hex(ascii_val)[2:] # remove 'Ox' prefix from the hex number
            char = "%" + hex_val
        
        output += char
    
    return output

print(get_url_encoding("this week's new blog post"))
