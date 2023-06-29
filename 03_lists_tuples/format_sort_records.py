def get_formatted_records(records):
    """
    Take a list of tuples with a specific structure
    and return the data as a readable, formatted string
    """
    output = ''
    
    for rec in records:
        first_name = rec[0]
        last_name = rec[1]
        time_2_dec = f"{rec[2]:.2f}"
        
        first_name_col_space = 10 - (len(first_name))
        last_name_col_space = 10 - (len(last_name))
        time_col_space = 5 - (len(time_2_dec))
        
        formatted_rec = (f"{last_name}{' ' * last_name_col_space}"
                         f"{first_name}{' ' * first_name_col_space}"
                         f"{' ' * time_col_space}{time_2_dec}")
        
        if rec == records[-1]: # no line break after last record
            output += formatted_rec
        else:   
            output += f"{formatted_rec}\n"
    
    return output

PEOPLE = [('Pippin', 'Took', 7.85),
         ('Samwise', 'Gamgee', 3.626),
         ('Frodo', 'Baggins', 10.603)]

print(get_formatted_records(PEOPLE))
