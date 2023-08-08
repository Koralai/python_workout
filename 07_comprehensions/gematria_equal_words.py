from gematria_calculate import get_gematria

def gematria_equal_words(word, ref_file):
    """
    Take a word and a reference file of many words. 
    Return a list of words from the reference file that have 
    an equal gematria value to the given word.
    """
    
    current_gematria_val = get_gematria(word)
    gm_equal_words = []
    
    with open(ref_file) as available_words:
        for file_word in available_words:
            if get_gematria(file_word.strip()) == current_gematria_val:
                gm_equal_words.append(file_word.strip())
                    
    return gm_equal_words

print(gematria_equal_words('cat', '07_comprehensions/words.txt'))
