def count_vowels(word):
    """Count the number of vowels in a word."""
    count = 0
    for letter in word:
        if letter.lower() in 'aeiouy':
            count +=1
    return count

def get_vowel_count(new_string):
    """
    Take a string and return a dictionary where the keys are the words, and
    the values are the number of vowels in each word.
    """
    return {word: count_vowels(word)
            for word in new_string.split()}
    
print(get_vowel_count('Abraham Lincoln was born in Kentucky.'))
