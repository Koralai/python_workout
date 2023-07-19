import os
from find_longest_word import find_longest_word

def find_all_longest_words(directory):
    """
    Search a directory and return a dict in which the keys are filenames
    and the values are the longest words from each file
    """
    
    longest_words = {}
    dir_contents = os.listdir(directory)
    
    for name in dir_contents:
        file_path = directory + name
        
        # skip directories
        if os.path.isdir(file_path) is True:
            continue
        
        longest_words[name] = find_longest_word(file_path)

    return longest_words

print(find_all_longest_words('02_strings/'))
