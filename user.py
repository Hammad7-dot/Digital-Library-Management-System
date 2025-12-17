class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = {}

    def borrow_book(self, book):
        if book.is_available():
            book.borrow()
            self.borrowed_books[book.book_id] = "Borrowed"
            return True
        return False

    def return_book(self, book):
        if book.book_id in self.borrowed_books:
            book.return_book()
            del self.borrowed_books[book.book_id]
            return True
        return False
