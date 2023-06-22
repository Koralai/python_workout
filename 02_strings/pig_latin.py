def pig_latin(word):
    """Take a word and convert it to pig latin, maintaining capitalization"""
    
    # check if the first letter is capitalized
    first_letter_capped = False
    if word[0].isupper() == True:
        first_letter_capped = True
            
    # if the word starts in a vowel, add "way" to the end
    if word[0].lower() in 'aeiouy':
        word = f"{word}way"
    
    # otherwise, put the first letter at the end of the word and add "ay"
    else:
        word = f"{word[1:]}{word[0]}ay"
    
    if first_letter_capped == True:
        return word.capitalize()
    return word
    
print(pig_latin("Happy"))
print(pig_latin("awesome"))
print(pig_latin("youthful"))
print(pig_latin("Mary"))