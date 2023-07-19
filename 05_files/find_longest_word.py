def exclude_word(word):
    """
    Return true if a word should be excluded; 
    return false if it doesn't need to be excluded.
    """
    
    if word[:4] == 'http':
        return True

    return False

def find_longest_word(filename):
    """Read a file and return the longest word in that file"""
    
    with open(filename, encoding='utf-8') as new_file:
        longest_word_length = 0
        longest_word = ''
        
        for line in new_file:
            words = line.split()
            
            for word in words:
                if len(word) > longest_word_length:
                    if exclude_word(word) is False:
                        longest_word = word
                        longest_word_length = len(word)
                    
    return longest_word

print(find_longest_word('02_strings/lamplighter.txt'))
