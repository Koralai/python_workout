def get_even_odd_sum(sequence):
    """
    Take a sequence of numbers and return a dictionary with the sum of the 
    even-indexed numbers and the sum of the odd-indexed numbers
    """
    
    output = {
        'even_sum': 0,
        'odd_sum': 0,
    }

    i = 0
    while i < len(sequence):
        current_num = sequence[i]
        if i % 2 == 0:
            output['even_sum'] += current_num
        else:
            output['odd_sum'] += current_num
        i += 1

    return output


sequence_1 = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
sequence_2 = (10, 4, 10, 4, 10, 4, 10, 4)
print(get_even_odd_sum(sequence_1))
print(get_even_odd_sum(sequence_2))
