class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_user(self, user):
        self.users[user.user_id] = user

    def search_book(self, keyword):
        results = []
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                results.append(book)
        return results

    def borrow_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
            return self.users[user_id].borrow_book(self.books[book_id])
        return False

    def return_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
            return self.users[user_id].return_book(self.books[book_id])
        return False
