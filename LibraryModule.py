# LibraryManager.py

# Initial book data
books = {
    "9780135175792": {
        "title": "Operating Systems: Internals and Design Principles",
        "author": "William Stallings",
        "publisher": "Pearson",
        "volume": "9th Edition",
        "year": 2020,
        "stock": 45
    },
    "9780134494166": {
        "title": "Operating System Concepts",
        "author": "Abraham Silberschatz, Greg Gagne, Peter B. Galvin",
        "publisher": "Wiley",
        "volume": "10th Edition",
        "year": 2020,
        "stock": 38
    },
    "9780262046009": {
        "title": "Structure and Interpretation of Computer Programs",
        "author": "Harold Abelson, Gerald Jay Sussman, Martin Henz",
        "publisher": "MIT Press",
        "volume": "2nd Edition",
        "year": 2022,
        "stock": 0
    },
    # Add remaining books here
}

def add_book(book):
    isbn = book["ISBN"]
    if isbn in books:
        print("Book already exists in the library.")
    else:
        books[isbn] = book
        print("Book added successfully.")

def remove_book(isbn):
    if isbn in books:
        del books[isbn]
        print("Book removed successfully.")
    else:
        print("ISBN not found in the library.")

def get_book_details(isbn):
    if isbn in books:
        return books[isbn]
    else:
        print("ISBN not found in the library.")
        return None

def search(title="",author=""):
    if title == "" and author == "":
        print("Your input in empty")

    elif author!="":
        for isbn,book in books.items():
            if author in book["author"]:
                print({isbn: book})

    else:
        for isbn, book in books.items():
            if title in book["title"]:
                print({isbn: book})


def list_books():
    return list(books.values())

def update_book(isbn, **kwargs):
    if isbn in books:
        for key, value in kwargs.items():
            if key in books[isbn]:
                books[isbn][key] = value
        print("Book details updated successfully.")
    else:
        print("ISBN not found in the library.")

def is_available(isbn):
    if isbn in books:
        return "Available" if books[isbn]["stock"] > 0 else "Not Available"
    else:
        print("ISBN not found in the library.")
        return "Not Available"

def print_books():
    print("Available Books:")
    for isbn, book_info in books.items():
        print(f"ISBN: {isbn} || Title: {book_info['title']} || Author: {book_info['author']}")



