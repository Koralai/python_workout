def get_formatted_records(records):
    """
    Take a list of tuples with a specific structure
    and return the data as a readable, formatted string
    """
    output = ''
    
    for rec in records:
        first_name_col_space = 10 - (len(rec[0]))
        last_name_col_space = 10 - (len(rec[1]))
        time_col_space = 5 - (len(f"{rec[2]:.2f}"))
        
        formatted_rec = (f"{rec[1]}{' ' * last_name_col_space}"
                         f"{rec[0]}{' ' * first_name_col_space}"
                         f"{' ' * time_col_space}{rec[2]:.2f}")
        
        if rec == records[-1]: # no line break after last record
            output += formatted_rec
        else:   
            output += f"{formatted_rec}\n"
    
    return output

PEOPLE = [('Pippin', 'Took', 7.85),
         ('Samwise', 'Gamgee', 3.626),
         ('Frodo', 'Baggins', 10.603)]

print(get_formatted_records(PEOPLE))
