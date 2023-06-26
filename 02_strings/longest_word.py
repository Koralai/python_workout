def get_longest_word(file):
    """Read a text file and return the longest word within the file"""
    
    text = open(file, encoding='utf-8').read()
    words = text.split()
    
    i = 0
    longest_word = words[i]
    word_length = len(longest_word)
        
    for word in words:
        if len(word) > word_length:
            if 'http' not in word:  # exclude urls
                longest_word = words[i]
                word_length = len(word)
        i += 1
    
    message = (f"The longest word in this file is '{longest_word}' " 
                f"with {word_length} letters.")
    
    return message


# Future improvements:
# strip out punctuation
