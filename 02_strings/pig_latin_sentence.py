def pig_latin(word):
    if word[0].lower() in 'aeiouy':
        return f"{word}way"
    
    return f"{word[1:]}{word[0]}ay"

def pl_sentence(sentence):
    """
    Take a series of words, separated by spaces, and convert them
    into pig latin
    """    
    sentence_words = sentence.split()
    pl_sentence_words = []
    
    for word in sentence_words:
        word = pig_latin(word)
        pl_sentence_words.append(word)
        
    return ' '.join(pl_sentence_words)

print(pl_sentence('the slings and arrows of outrageous fortune'))