from get_words_set import get_words_set

excluded_words = get_words_set('05_files/word_count_project/excluded_words.txt')

def strip_punctuation(word):
    """Strip out initial and final punctuation from a word"""
    if word[-1] in '?!;.,:"”)':
        word = word[:-1]
    if word[0] in '("“':
        word = word[1:]
    
    return word

def get_word_count(filename):
    """
    Read a file and return a dictionary where the key is a word and the
    value is the number of times that word appears in the file.
    Allow for excluded words ("the", "a", etc).
    """
    word_count = {}
    
    with open(filename, encoding='utf-8') as new_file:
        for line in new_file:
            words = line.split()
            
            for word in words:
                word = strip_punctuation(word)
                
                if word.lower() not in excluded_words:        
                    # increment the count for that word 
                    word_count[word] = word_count.get(word, 0) + 1
    
    return word_count
