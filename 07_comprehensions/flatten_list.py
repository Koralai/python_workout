def flatten_list(list_of_lists):
    """Take a list of lists and return all data as a single list."""
    
    output = [item 
              for one_list in list_of_lists
              for item in one_list]
            
    return output

my_list = [[1,2],[3,4]]

print(flatten_list(my_list))
