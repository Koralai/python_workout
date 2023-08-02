def find_sum_numbers(string):
    """
    Take a string and return the sum of all numbers in the string
    (i.e., the word contains no digits)
    """
    items = string.split()
    output = [item 
              for item in items
              if item.isdigit() is True]
    
    return output

my_string = 'high score 99 low score 62 class 7b'
print(find_sum_numbers(my_string))
