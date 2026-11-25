class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
        else:
            print("Book not found")

    def list_books(self):
        print("Books:", self.__books)

l = Library()

l.add_book("Python")
l.add_book("Java")
l.add_book("C++")

l.list_books()

l.remove_book("Java")

l.list_books()