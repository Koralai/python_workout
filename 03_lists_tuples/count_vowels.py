def count_vowels(word):
    """Return the number of vowels in a word"""
    count = 0
    for char in word:
        if char.lower() in 'aeiou':
            count +=1
    return count

def sort_by_num_vowels(str_list):
    """Sort a list of strings by how many vowels each string contains"""
    
    return sorted(str_list, key=count_vowels)


new_list = ['ohio', 'wyoming', 'rhode island', 'new york', 'arizona',]
print(sort_by_num_vowels(new_list))
