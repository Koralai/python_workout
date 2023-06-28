def compare_words(word_1, word_2):
    """Compare two words and return them in a list, in alpha order"""
    
    output = []
    
    i = 0
    while True:
        word_1_lett = word_1.lower()[i]
        word_2_lett = word_2.lower()[i]
        
        if ord(word_1_lett) < ord(word_2_lett):
            output = [word_1, word_2]
            break
        if ord(word_2_lett) < ord(word_1_lett):
            output = [word_2, word_1]
            break
        i += 1
    
    return output
    

def alphabetize_names(list_of_dicts):
    """
    Take a list of dictionaries containing first and last names.
    Return the same list of dictionaries sorted alphabetically 
    (by last name, then by first name).
    """
    
    output = []
    
    


def main():
    print(compare_words('acrimonious', 'acre'))

if __name__ == '__main__':
    main()
