def pig_latin(word):
    """Take a word and convert it to pig latin"""
    
    # if the word starts in a vowel, add "way" to the end
    if word[0].lower() in 'aeiouy':
        word += "way"
        return word
    
    # otherwise, put the first letter at the end of the work and add "ay"
    else:
        first_letter = word[0]
        word = word[1:] + first_letter + "ay"
        return word
    
print(pig_latin("happy"))
print(pig_latin("awesome"))