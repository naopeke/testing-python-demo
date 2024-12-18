class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name 
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book: {self.name}, {self.book_type}, weighting {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)
    
    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)
    
#book = Book("Harry Potter", "hardcover", 3380)
book = Book.hardcover("Harry Potter", 3380)
book2 = Book.paperback("Python 101", 600)

print(Book.TYPES)
print(book)
print(book2)