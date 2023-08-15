class Book:
    def __init__(self, title, author_fname, author_lname, price):
        self.title = title
        self.author_fname = author_fname
        self.author_lname = author_lname
        self.price = float(price)

class Shelf:
    def __init__(self):
        self.current_books = []
        
    def add_book(self, *new_books: Book):
        for one_book in new_books:
            self.current_books.append(one_book)
    
    def total_price(self):
        price = float(0)
        for one_book in self.current_books:
            price += one_book.price
        return price
    
    def has_book(self, book_title: str):
        for one_book in self.current_books:
            if one_book.title == book_title.lower():
                return True
        return False
    
    def __repr__(self):
        titles = [one_book.title
                  for one_book in self.current_books]
        return f"Books on this shelf: {', '.join(titles).title()}" 
