def pig_latin(word):
    """Convert a word into pig Latin."""
    
    if word[0].lower() in 'aeiouy':
        return f"{word}way"
    
    return f"{word[1:]}{word[0]}ay"

def file_to_pig_latin(file_name):
    """Read a file and return the file's contents translated into pig Latin."""
    
    output = ""
    
    with open(file_name, encoding='utf-8') as read_file:
        for one_line in read_file:
            words = one_line.split()
            for word in words:
                output += f"{pig_latin(word)} "
                
    return output
                        
print(file_to_pig_latin('02_strings/sun_also_rises.txt'))
