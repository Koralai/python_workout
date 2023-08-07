def is_supervocalic(word):
    """Return "True" if a word is supervocalic, "False" if not."""
    all_vowels = {'a','e','i','o','u'}
    word_vowels = set()
    
    for letter in word.lower():
        if letter in 'aeiou':
            word_vowels.add(letter)
    
    if all_vowels == word_vowels:
        return True
    return False

def find_supervocalic_words(file_name):
    """
    Read a file that contains one word per line. Return a set of all
    supervocalic words in the file (i.e., words that contain all
    five vowels).
    """
    
print(is_supervocalic('boatbuilder'))
