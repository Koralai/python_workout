def word_data(*words):
    """
    Takes an unspecified number of words, and returns three data points:
    the length of the shortest word, the length of the longest word, and the
    average word length
    """
    
    # collect the word lengths in a list
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))     
    
    # sort the list   
    word_lengths.sort()
        
    # now we know the shortest and longest words
    shortest_word = word_lengths[0]
    longest_word = word_lengths[-1]
    
    # get the average word length
    word_lengths_total = 0
    for number in word_lengths:
        word_lengths_total += number    
    average_word_length = word_lengths_total/len(word_lengths)
    
    return (shortest_word, longest_word, round(average_word_length))

print(word_data('ohio', 'arizona', 'california', 'mississippi', 'vermont', 'utah'))
