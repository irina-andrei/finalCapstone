# A python file that that can be used by a bookstore clerk. The program allows
# adding new books to the database, updating book information, deleting books 
# from the database and searching the database to find a specific book.


import sqlite3
my_db = sqlite3.connect('ebookstore')
# Using the .connect() function to connect to the database 'ebookstore'.


#=====Formatting Options=====
GREEN = '\033[92m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
RED = '\033[31m'
ENDC = '\033[0m' # Removes all formatting applied.
EM = f"{RED}‼{ENDC}" 
# 'Exclamation Mark' shorthand, preventing repeat code or going over 79char.


def enter_book():
    """ Function will add a new entry to the 'books' table in database.
    Parameters: None
    Returns: None """
    #books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)
    
    new_id = last_id + 1
    # Finding the last id used in the table and generating a new id number.
    
    title = input("Enter the title of the new book: ")
    author = input("Enter the author: ")
    quantity = int(input("Enter quantity: "))
    # Getting all the new book details from user.
    
    cursor.execute('''INSERT INTO books VALUES(?,?,?,?)''', 
                (new_id, title, author, quantity))
    # Adding new book to table.
    print(f"\n{GREEN}New book saved!{ENDC} The new entry:")
    
    cursor.execute('''SELECT id, Title, Author, Qty FROM books 
            WHERE id=?''', (new_id,))
    for row in cursor:
        print('ID{0}: {1} ({2}) - Qty {3}'.format(row[0], 
                row[1], row[2], row[3]))
    # Confirming to user the details of the new entry.
    
    my_db.commit()
    # Commiting our changes.


def update_book():
    """ Function will update entries in the 'books' table in database.
    Parameters: None
    Returns: None """
    
    book_id = int(input("Enter the ID of the book you want to update: "))
    quantity = int(input("Enter new quantity for book: "))
    # Getting id for book and new quantity from user. 
    
    cursor.execute('''UPDATE books SET Qty = ? 
                WHERE id = ? ''', (quantity, book_id))
    # Updating the table with the new quantity for the book based on id.
    
    my_db.commit()
    # Commiting our changes. 
    
    print(f"\n{GREEN}Quantity updated!{ENDC} New quantity: {quantity}.")


def delete_book():
    """ Function will delete a book from the 'books' table in database.
    Parameters: None
    Returns: None """
    
    book_id = int(input("Enter the ID of the book you want to delete: "))
    
    print(f"\n{RED}This entry will be deleted:{ENDC}")
    cursor.execute('''SELECT id, Title, Author, Qty FROM books 
            WHERE id=?''', (book_id,))
    # Looking up the entry received from user.
    for row in cursor:
        print('ID{0}: {1} ({2}) - Qty {3}'.format(row[0], 
            row[1], row[2], row[3]))
    # Confirming the entry that will be deleted.
    
    cursor.execute('''DELETE FROM books WHERE id = ? ''', (book_id,))
    # Deleting the book from table.
    print(f"\nBook successfully {RED}deleted{ENDC}.")
    
    my_db.commit()
    # Commiting our changes.


def search_book():
    """ Function will search for a book in the database by id, title or author.
    Parameters: None
    Returns: None """
    
    while True:
        choice = input(f'''
        {BLUE}╔{'═'*29}╗
        ║{ENDC} Enter your search criteria: {BLUE}║
        ║ ♦{CYAN} 1 {ENDC}- id {BLUE}{' '*19}║
        ║ ♦{CYAN} 2 {ENDC}- title {BLUE}{' '*16}║
        ║ ♦{CYAN} 3 {ENDC}- author {BLUE}{' '*15}║
        ╚{'═'*29}╝
        {ENDC}  Your selection: {CYAN}''')
        
        print(f"{ENDC}", end='') # Resetting the colour formatting. 
        
        if choice == '1':
            # Searching by id.
            id_search = input(f"Enter the id you want to search: {CYAN}")
            
            print(f"\n{PINK}Search results:{ENDC}")
            
            cursor.execute('''SELECT id, Title, Author, Qty FROM books 
                WHERE id=?''', (id_search,))
            # Searching for book.
            for row in cursor:
                print('ID{0}: {1} ({2}) - Qty {3}'.format(row[0], 
                    row[1], row[2], row[3]))
            # Prints out the entries found, if any.
            
            cursor.execute('''SELECT id, Title, Author, Qty FROM books 
                WHERE id=?''', (id_search,))
            # Searches again in case there weren't any matches.
            if cursor.fetchone() is None:
                print(f"{EM} No entries matching your request.")
            # If it doesn't find any entries, prints out there's no matches.
            
            break
        
        elif choice == '2':
            # Searching by title.
            title = input(f"Enter the title you want to search: {CYAN}")
            
            print(f"\n{PINK}Search results:{ENDC}")
            
            cursor.execute('''SELECT id, Title, Author, Qty FROM books 
                WHERE Title=?''', (title,))
            # Searching for book.
            for row in cursor:
                print('ID{0}: {1} ({2}) - Qty {3}'.format(row[0], 
                    row[1], row[2], row[3]))
            # Prints out the entries found, if any.
            
            cursor.execute('''SELECT id, Title, Author, Qty FROM books 
                WHERE Title=?''', (title,))
            # Searches again in case there weren't any matches.
            if cursor.fetchone() is None:
                print(f"{EM} No entries matching your request.")
            # If it doesn't find any entries, prints out there's no matches.
            
            break
        
        elif choice == '3':
            # Searching by author.
            author = input(f"Enter the author you want to search: {CYAN}")
            
            print(f"\n{PINK}Search results:{ENDC}")
            
            cursor.execute('''SELECT id, Title, Author, Qty FROM books 
                WHERE Author=?''', (author,))
            # Searching for book.
            for row in cursor:
                print('ID{0}: {1} ({2}) - Qty {3}'.format(row[0], 
                    row[1], row[2], row[3]))
            # Prints out the entries found, if any.
            
            cursor.execute('''SELECT id, Title, Author, Qty FROM books 
                WHERE Author=?''', (author,))
            # Searches again in case there weren't any matches.
            if cursor.fetchone() is None:
                print(f"{EM} No entries matching your request.")
            # If it doesn't find any entries, prints out there's no matches.
            
            break
        
        else:
            print(f"\n{EM} You have made a wrong choice, please try again.")


cursor = my_db.cursor()  
# Getting a cursor object.

cursor.execute('''
    CREATE TABLE IF NOT EXISTS 
        books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)
''')
# Creating a table called 'books' with id as the primary key.

my_db.commit()
# Commiting our changes. 


stock = [(3001, 'A Tale of Two Cities', 'Charles Dickens', 30), 
    (3006, 'Great Expectations', 'Charles Dickens', 23), 
    (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40), 
    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25), 
    (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37), 
    (3007, 'The Lord of the Rings', 'J.R.R', 3), 
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)]
# A list with all the books that will be saved in the database. 

cursor.executemany('''INSERT INTO books(id, Title, Author, Qty)
                VALUES (?, ?, ?, ?)''', stock)
# Book stock inserted into the 'books' table.

last_id = 3007
# Saving the last id used for use when creating new entries to table.

my_db.commit()
# Commiting our changes. 

print(f"\n{GREEN}All books inserted into database:{ENDC}")
cursor.execute('''SELECT id, Title, Author, Qty FROM books''')
for row in cursor:
    print('ID{0}: {1} ({2}) - Qty {3}'.format(row[0], row[1], row[2], row[3]))


while True:
    menu = input(f'''
    {PINK}╔{'═'*45}╗
    ║{ENDC} Please select one of the following options: {PINK}║
    ║ ♦{CYAN} 1 {ENDC}- Enter book {PINK}{' '*27}║
    ║ ♦{CYAN} 2 {ENDC}- Update book {PINK}{' '*26}║
    ║ ♦{CYAN} 3 {ENDC}- Delete book {PINK}{' '*26}║
    ║ ♦{CYAN} 4 {ENDC}- Search books {PINK}{' '*25}║
    ║ ♦{RED} 0 {ENDC}- Exit{ENDC}{PINK}{' '*34}║
    ╚{'═'*45}╝
    {ENDC}  Your selection: {CYAN}''')
    
    print(f"{ENDC}", end='') # Resetting the colour formatting. 
    
    if menu == '1':
        # Entering a new book to database.
        enter_book()
        last_id += 1
        # Updating the last id used.
    
    elif menu == '2':
        # Updating a book in the database.
        update_book()
    
    elif menu == '3':
        # Deleting a book from database.
        delete_book()
    
    elif menu == '4':
        # Searches for a book in database.
        search_book()
    
    elif menu == '0':
        # This will exit program.
        
        # Loading and printing all the books in the table for a final check.
        cursor.execute('''SELECT id, Title, Author, Qty FROM books''')
        searched_list = cursor.fetchall()
        print(f"\n{PINK}Final status of database:{ENDC}")
        print(f"{BLUE}(id, Title, Author, Qty){ENDC}")
        for bk in searched_list:
            print(bk)
        
        
        my_db.commit()
        my_db.close()
        # Comitting and closing the database connection.
        print(f"\n{RED}Connection to database closed.{ENDC}")
        print(f"{CYAN}Goodbye!{ENDC}")
        break
    
    else:
        print(f"\n{EM} You have made a wrong choice, please try again.")