
from LibraryModule import*
sample_books = [
    {
        "ISBN": "9781492051367",
        "title": "Fluent Python: Clear, Concise, and Effective Programming",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "volume": "2nd Edition",
        "year": 2021,
        "stock": 40
    },
   {
       "ISBN": "9780135957059",
       "title": "Effective Python: 59 Specific Ways to Write Better Python",
       "author": "Brett Slatkin",
       "publisher": "Pearson",
        "volume": "2nd Edition",
        "year": 2020,
        "stock": 50
    }
    ]
print("______________________________________________________________________________________________________________")
print("Question 1")

print(f"The number of books in library are {len(books)}")
for book in sample_books:
    add_book(book)

print(f"The number of books in library are {len(books)}")

print("______________________________________________________________________________________________________________")
print("Question 2")

print("Remove a book")
print("Removing a book with ISBN 9780134494166:")
remove_book("9780134494166")
print(f"The number of books in library are {len(books)}")

print("______________________________________________________________________________________________________________")
print("Question 3")

print("Get book details")
print("Getting details of a book with ISBN 9780135175792:")
book_details = get_book_details("9780135175792")
print(book_details)

print("______________________________________________________________________________________________________________")
print("Question 4")

print("Search books")
print("Searching for books with title 'Operating Systems':")
print(search(title="Operating Systems"))

print(
        "______________________________________________________________________________________________________________")
print("Question 5")

print("Update book details")
print("Updating the stock of book with ISBN 9780135175792:")
update_book("9780135175792", stock=50)


print("______________________________________________________________________________________________________________")
print("Question 6")

print("Check availability")
print("Checking availability of book with ISBN 9780135175792:")
availability = is_available("9780135175792")
print(availability)

print("______________________________________________________________________________________________________________")
print("Question 7")

print("Print all books")
print_books()

print("______________________________________________________________________________________________________________")
