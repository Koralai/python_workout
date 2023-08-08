def book_data_to_dict(book_data):
    """
    Take a list of tuples containing book data and restructure it as
    a list of dictionaries.
    """
    
    return [{book[2]: 
            {'lname': book[0], 'fname': book[1], 'price':book[3]}
            }
             for book in book_data]
