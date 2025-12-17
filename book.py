class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def is_available(self):
        return self.available_copies > 0

    def borrow(self):
        if self.is_available():
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        self.available_copies += 1
