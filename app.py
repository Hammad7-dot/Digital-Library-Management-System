import streamlit as st
from library import Library
from user import User
from book import Book


st.set_page_config(page_title="Digital Library", layout="centered")
st.title("📚 Digital Library Management System")

# Initialize Library
if "library" not in st.session_state:
    st.session_state.library = Library()

library = st.session_state.library

menu = st.sidebar.selectbox("Menu", ["Add Book", "Add User", "Search Books", "Borrow Book", "Return Book", "View Records"])


# ADD BOOK
if menu == "Add Book":
    st.subheader("➕ Add New Book")
    book_id = st.text_input("Book ID")
    title = st.text_input("Title")
    author = st.text_input("Author")
    copies = st.number_input("Number of Copies", min_value=1, step=1)

    if st.button("Add Book"):
        library.add_book(Book(book_id, title, author, copies))
        st.success("Book added successfully")

# ADD USER
elif menu == "Add User":
    st.subheader("👤 Add User")
    user_id = st.text_input("User ID")
    name = st.text_input("User Name")

    if st.button("Add User"):
        library.add_user(User(user_id, name))
        st.success("User added successfully")

# SEARCH BOOK
elif menu == "Search Books":
    st.subheader("🔍 Search Books")
    keyword = st.text_input("Enter title or author")

    if keyword:
        results = library.search_book(keyword)
        if results:
            for book in results:
                st.write(f"**{book.title}** by {book.author} | Available: {book.available_copies}")
        else:
            st.warning("No books found")

# BORROW BOOK
elif menu == "Borrow Book":
    st.subheader("📖 Borrow Book")
    user_id = st.text_input("User ID")
    book_id = st.text_input("Book ID")

    if st.button("Borrow"):
        if library.borrow_book(user_id, book_id):
            st.success("Book borrowed successfully")
        else:
            st.error("Borrow failed (check availability or IDs)")

# RETURN BOOK
elif menu == "Return Book":
    st.subheader("📦 Return Book")
    user_id = st.text_input("User ID")
    book_id = st.text_input("Book ID")

    if st.button("Return"):
        if library.return_book(user_id, book_id):
            st.success("Book returned successfully")
        else:
            st.error("Return failed")

# VIEW RECORDS
elif menu == "View Records":
    st.subheader("📊 Borrowed Books Record")
    for user in library.users.values():
        st.write(f"👤 **{user.name}**")
        if user.borrowed_books:
            for book_id, date in user.borrowed_books.items():
                st.write(f"- Book ID: {book_id}, Borrowed on: {date}")
        else:
            st.write("No books borrowed")

















            