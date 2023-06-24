"""Read a text file and return a nonsensical sentence from words in the file"""

import random

def nonsense_sentence(file, words_in_sentence, every_nth_word):    
    file_text = open(file, encoding='utf-8').read()    
    file_text_words = file_text.split()    
    
    nonsense_sentence_words = []    

    starting_word_index_range = round(len(file_text_words) * 0.4)
    starting_word_index = random.randint(0, starting_word_index_range)    
    last_word_index = starting_word_index + (words_in_sentence * every_nth_word)
    
    for i in range(starting_word_index, last_word_index, every_nth_word):
        nonsense_sentence_words.append(file_text_words[i])
    
    final_string = ' '.join(nonsense_sentence_words)
    
    final_sting_formatted = ''
    punctuation = '""“”,!.;:?'
    
    for character in final_string:
        if character not in punctuation:
            final_sting_formatted += character
        
    return f"{final_sting_formatted.capitalize()}."

print(nonsense_sentence('lamplighter.txt', 15, 78))
