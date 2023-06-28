def get_first_last(sequence):
    """
    Take a sequence and return the first and last elements of that sequence,
    in a two-element sequence of the same type (e.g, [1,2,3,4] returns [1,4])
    """
    return sequence[:1] + sequence[-1:]


print(get_first_last('apple'))
print(get_first_last(['hi', 'bye', 'here', 'there']))
print(get_first_last((1, 4, 7, 8, 19, 20)))
