def pl_sentence(sentence):
    """Take a series of words and convert them into pig latin"""

    pl_sentence_words = []
    
    for word in sentence.split():
        if word[0].lower() in 'aeiouy':
            pl_sentence_words.append(f"{word}way")
        else:
            pl_sentence_words.append(f"{word[1:]}{word[0]}ay")
        
    return ' '.join(pl_sentence_words)

print(pl_sentence('the slings and arrows of outrageous fortune'))