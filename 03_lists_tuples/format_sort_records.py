from operator import itemgetter

def get_formatted_records(records):
    """
    Take a list of tuples with a specific structure
    and return the data as a readable, formatted string
    """
    output = ''
    
    # sort records by last name, first name (indexes 1 and 0 in the data)
    sorted_records = sorted(records, key=itemgetter(1,0))
    
    for rec in sorted_records:
        first_name = rec[0]
        last_name = rec[1]
        time = rec[2]
        
        formatted_rec = (f"| {last_name:10}"
                         f"| {first_name:10}"
                         f"| {time:5.2f} |")
        
        if rec == sorted_records[-1]: # no line break after last record
            output += formatted_rec
        else:   
            output += f"{formatted_rec}\n"
    
    return output

HOBBITS = [('Pippin', 'Took', 7.85),
         ('Samwise', 'Gamgee', 3.626),
         ('Frodo', 'Baggins', 10.603),
         ('Bilbo', 'Baggins', 15.985)]

print(get_formatted_records(HOBBITS))
