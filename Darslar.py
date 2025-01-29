class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        book = {
            "title": title,
            "author": author,
            "year": year
        }
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
<<<<<<< HEAD

catalog = Catalog()
=======
catalog = Catalog()

>>>>>>> b9b365f1c138de6689d36baa62625dba1ac9e035
catalog.add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
catalog.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
catalog.add_book("1984", "George Orwell", 1949)

catalog.display_books()
