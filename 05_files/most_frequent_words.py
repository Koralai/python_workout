from get_words_set import get_words_set

excluded_words = get_words_set('05_files/excluded_words.txt')

def get_most_frequent_words(filename):
    """
    Read a file and return the most frequent, meaningful words in that file
    """
    word_count = {}
    
    with open(filename, encoding='utf-8') as new_file:
        for line in new_file:
            words = line.split()
            
            for word in words:
                if word not in excluded_words:
                    # increment the count for that word 
                    word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

print(get_most_frequent_words('05_files/wcfile.txt'))
