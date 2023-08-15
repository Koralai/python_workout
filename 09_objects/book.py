class Book:
    def __init__ (self, title, author_fname, author_lname, price):
        self.title = title
        self.author_fname = author_fname
        self.author_lname = author_lname
        self.price = float(price)

class Shelf:
    def __init__(self):
        self.current_books = []
        
    def add_book(self, new_book: Book):
        return self.current_books.append(new_book)
    
    def total_price(self):
        price = float(0)
        for one_book in self.current_books:
            price += one_book.price
        return price

b_1 = Book('the merchant of venice', 'william', 'shakespeare', 10)
b_2 = Book('beloved', 'toni', 'morrison', 14)
b_3 = Book('little women', 'louisa may', 'alcott', 9)

print(b_1.price)
