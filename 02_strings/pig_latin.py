def pig_latin(word):
    """Take a word and convert it to pig latin"""
    
    # if the word starts in a vowel, add "way" to the end
    if word[0].lower() in 'aeiouy':
        return f"{word}way"
    
    # otherwise, put the first letter at the end of the word and add "ay"
    return f"{word[1:]}{word[0]}ay"
    
print(pig_latin("happy"))
print(pig_latin("awesome"))
print(pig_latin("youthful"))