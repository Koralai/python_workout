import gematria_key as gk

def get_gematria(word):
    """Return the gematria value of a word."""
    gematria_value = 0
    
    for letter in word.lower():
        gematria_value += gk.GEMATRIA_KEY[letter]
    
    return gematria_value
