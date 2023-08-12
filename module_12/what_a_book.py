# Import statements
import sys
import mysql.connector
from mysql.connector import errorcode

# database config object 
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# Displays the main menu
def show_menu():
    print("\n  Main Menu\n")

    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit")
    # User main menu input
    try:
        choice = int(input('      Enter 1-4: '))

        return choice
    except ValueError:
        print("\n  Invalid number\n")

# Display books in Main Menu
def show_books(_cursor):

    _cursor.execute("SELECT book_id, book_name, author, details from book")

    books = _cursor.fetchall()

    print("\n  Viewing Books\n")

    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

# Display locations in Main Menu
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n  Displaying Store Locations\n")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))

# Customer ID error detection and input
def validate_user():
    try:
        user_id = int(input('\n      Enter customer_id 1-3: '))

        if user_id < 0 or user_id > 3:
            print("\n  Invalid customer number\n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  Invalid number\n")

        sys.exit(0)

# View Account Menu
def show_account_menu():
    """ display the users account menu """

    try:
        print("\n      Customer Menu\n")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        Enter 1-3: '))

        return account_option
    except ValueError:
        print("\n  Invalid number\n")

        sys.exit(0)

# View Wishlist
def show_wishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n        Displaying Wishlist\n")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

# View books not added to wishlist
def show_books_to_add(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        Displaying Books\n")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

# Add books to wishlist
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    if book_id >= 1 and book_id <= 9:
        _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))
        db.commit()
        print("\n        Book id: {} was added to your wishlist!".format(book_id))
    else:
        print("Please enter a valid book ID!")

# Connect to database
try:

    db = mysql.connector.connect(**config) 

    cursor = db.cursor() 

    print("\n  Welcome to Whatabook!\n")

    user_selection = show_menu() 

# User main menu selections
    while user_selection != 4:
        # Press 1 to show books
        if user_selection == 1:
            show_books(cursor)
        # Press 2 to show locations
        if user_selection == 2:
            show_locations(cursor)
        # Press three to go to account menu
        if user_selection == 3:
            # Ensure ID is valid
            my_user_id = validate_user()
            # Show account menu
            account_option = show_account_menu()
            # While not exiting..
            while account_option != 3:
                # View customer wishlist
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                # Add book to wishlist
                if account_option == 2:

                    show_books_to_add(cursor, my_user_id)

                    # Input wishlist book
                    book_id = int(input("\n        Enter the id of the book you want to add: "))
                    
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                # Detect valid menu input
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please retry...")
                # Go back to account menu
                account_option = show_account_menu()

        # Detect valid menu input
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please retry...")
        # Go back to main menu
        user_selection = show_menu()

    print("\n\n  Program terminated...")

# Valid account and database error detection
except mysql.connector.Error as err:
    """ handle errors """ 
    # Check valid username/password
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    # Check if database exists
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    # Close database connection
    db.close()