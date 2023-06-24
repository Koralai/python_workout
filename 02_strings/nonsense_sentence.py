"""Read a text file and return a nonsensical sentence from words in the file"""

def nonsense_sentence(file, start_with_nth_word, words_in_sentence, nth_step):
    
    file_text = open(file, encoding='utf-8').read()    
    file_text_words = file_text.split()    
    
    nonsense_sentence_words = []
    first_word = start_with_nth_word
    total_steps = nth_step * words_in_sentence
    
    for i in range(first_word, total_steps, nth_step):
        nonsense_sentence_words.append(file_text_words[i])
    
    final_sentence = ' '.join(nonsense_sentence_words)
    
    return f"{final_sentence.capitalize()}."

print(nonsense_sentence('sun_also_rises.txt', 68, 15, 20))
