from book_data_orig import sci_fi_books

def book_data_to_dict(book_data):
    """
    Take a list of tuples containing book data and restructure it as
    a list of dictionaries.
    """
    
    return [{book[2]: 
            {'lname': book[0], 'fname': book[1], 'price':book[3]}
            }
             for book in book_data]

print(book_data_to_dict(sci_fi_books))
