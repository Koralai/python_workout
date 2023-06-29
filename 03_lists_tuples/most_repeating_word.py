from collections import Counter 

def count_most_repeated_letter(word):
    """
    Find the most common letter in a word and return the number of times
    it occurs
    """
    return Counter(word.lower()).most_common(1)[0][1]

def get_most_repeated_letter(word):
    """Return the most common letter in a word"""
    return Counter(word.lower()).most_common(1)[0][0]

def get_most_repeating_word(list_words):
    """
    Take a sequence of strings and return the string that contains the
    greatest number of repeated letters
    """
    
    most_repeating_word = ''
    repeated_letter = ''
    highest_letter_ct = 0
    
    for word in list_words:
        current_letter_ct = count_most_repeated_letter(word)
        
        if current_letter_ct > highest_letter_ct:
            most_repeating_word = word
            highest_letter_ct = current_letter_ct
            repeated_letter = get_most_repeated_letter(word)
    
    message = (f'The word "{most_repeating_word}" contains the letter '
                f'"{repeated_letter}" {highest_letter_ct} times.')
    
    return message
        

new_list = ['alaska', 'delaware', 'iowa', 'colorado']

print(get_most_repeating_word(new_list))
