from book import Book
from book import Shelf

b_1 = Book('the merchant of venice', 'william', 'shakespeare', 10)
b_2 = Book('beloved', 'toni', 'morrison', 14)
b_3 = Book('little women', 'louisa may', 'alcott', 9)

shelf_1 = Shelf()
shelf_1.add_book(b_1, b_2)
shelf_1.add_book(b_3)
print(shelf_1)
print(f"Total cost of the books on this shelf: ${shelf_1.total_price():.2f}")
print(shelf_1.has_book('romeo and juliet'))
print(shelf_1.has_book('Little Women'))
