def join_numbers(int_range):
    """
    Take a range of integers and return those numbers as a string,
    with commas between the numbers.
    """
    
    all_nums = [str(x) for x in range(int_range)]
    return ','.join(all_nums)

print(join_numbers(15))
