# DIGITAL LIBRARY MANAGEMENT SYSTEM

Project Type: Python Mini Project
Concepts Used: Object-Oriented Programming (OOP)
Interface: Streamlit (GUI)

## PROJECT DESCRIPTION

This project is a Digital Library Management System developed using Python and core Object-Oriented Programming (OOP) concepts. The system allows users to manage books in a library, search for books, borrow and return books, and check book availability through a menu-driven Streamlit graphical user interface.

The main purpose of this project is to demonstrate the use of classes, objects, and encapsulation in a real-world application.
## PROJECT STRUCTURE

The project folder contains the following files:

1. app.py        -> Main Streamlit application file (GUI)
2. book.py       -> Book class definition
3. user.py       -> User class definition
4. library.py    -> Library class definition
5. README.txt    -> Project documentation (this file)

## CLASSES OVERVIEW

1. Book Class

* Attributes:
  * Book ID
  * Title
  * Author
  * Total Copies
  * Available Copies
* Functions:

  * Check availability
  * Borrow book
  * Return book

2. User Class

* Attributes:
  * User ID
  * User Name
  * Borrowed Books

* Functions:
  * Borrow book
  * Return book

3. Library Class
  * Responsibilities
  * Maintain all book records
  * Register users
  * Search books by title or author
  * Handle borrow and return operations
  
## FEATURES IMPLEMENTED

* Add New Book
* Search Book by Title
* Search Book by Author
* Borrow Book
* Return Book
* View All Books
* Check Book Availability
