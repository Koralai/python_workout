def get_words_set(filename):
    """
    Read a file of words (one word per line) 
    and return a set containing those words
    """
      
    words_set = set()
    with open(filename, encoding='utf-8') as word_list:
        for line in word_list:
            word = line.split()
            words_set.update(word)
    
    return words_set
