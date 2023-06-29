def get_formatted_records(records):
    """
    Take a list of tuples with a specific structure
    and return the data as a readable, formatted string
    """
    output = ''
    
    for rec in records:
        formatted_rec = f"{rec[1]} {rec[0]} {rec[2]:.2f}"
        if rec == records[-1]: # no line break after last record
            output += formatted_rec
        else:   
            output += f"{formatted_rec}\n"
    
    return output

PEOPLE = [('Pippin', 'Took', 7.85),
         ('Samwise', 'Gamgee', 3.626),
         ('Frodo', 'Baggins', 10.603)]

print(get_formatted_records(PEOPLE))
