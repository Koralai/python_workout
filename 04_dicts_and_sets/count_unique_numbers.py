def count_unique_numbers(list_nums):
    """
    Accept a list of numbers and return a count of unique numbers in the list
    """
    
    # empty set
    unique_nums = set()
    
    # update the set with the list of numbers (will keep unique values only)
    unique_nums.update(list_nums)
    
    return len(unique_nums)

birth_years = [1993, 2017, 2003, 2003, 1993, 2018, 2017, 1993]

print(count_unique_numbers(birth_years))
