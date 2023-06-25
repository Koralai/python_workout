def get_in_ubbi_dubbi(word):
    output = ''

    for letter in word.lower():
        if letter in 'aeiouy':
            letter = 'ub' + letter
        output += letter
    
    return output
