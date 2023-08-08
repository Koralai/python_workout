from gematria_calculate import get_gematria

def gematria_equal_words(word, ref_file):
    """
    Take a word and a reference file of many words. 
    Return a list of words from the reference file that have 
    an equal gematria value to the given word.
    """
    
    current_gematria_val = get_gematria(word)
                    
    return [one_word.strip()
            for one_word in open(ref_file)
            if get_gematria(one_word.strip()) == current_gematria_val]

print(gematria_equal_words('landrover', '07_comprehensions/words.txt'))
