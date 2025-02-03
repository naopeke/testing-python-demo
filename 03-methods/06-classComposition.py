# class BookShelf:
#     def __init__(self, quantity):
#         self.quantity = quantity
    
#     def __str__(self):
#         return f"BookShelf with {self.quantity} books."

# shelf = BookShelf(300)
# print(shelf) # BookShelf with 300 books.

# class Book(BookShelf):
#     def __init__(self, name, quantity):
#         super().__init__(quantity)
#         self.name = name

#     def __str__(self):
#         return f"Book {self.name}"

# book = Book("Harry Potter", 120)
# print(book) # BookShelf with 120 books.

class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f"BookShelf with {len(self.books)} books."

class Book:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Book {self.name}"

book = Book("Python 101")
book2 = Book("Typescript")
shelf = BookShelf(book, book2)

print(shelf)