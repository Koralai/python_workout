from collections import Counter 

def get_most_repeating_word(list_words):
    """
    Take a sequence of strings and return the string that contains the
    greatest number of repeated letters
    """
    
    most_repeating_word = ''
    repeated_letter = ''
    highest_letter_ct = 0
    
    for word in list_words:
        # letters by how often they appear, in descending order:
        letters_by_frequency = Counter(word.lower()).most_common()
        
        # number of times the most common letter appears in the word:
        current_letter_ct = letters_by_frequency[0][1] 
        
        if current_letter_ct > highest_letter_ct:
            most_repeating_word = word
            highest_letter_ct = current_letter_ct
            repeated_letter = letters_by_frequency[0][0]
    
    message = (f'The word "{most_repeating_word}" contains the letter '
                f'"{repeated_letter}" {highest_letter_ct} times.')
    
    return message
        

new_list = ['alaska', 'delaware', 'iowa', 'colorado']

print(get_most_repeating_word(new_list))
