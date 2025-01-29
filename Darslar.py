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


catalog = Catalog()

catalog = Catalog()


catalog.add_book("The 43534534 Gatsby", "F. Scott Fitzgerald", 1925)
catalog.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
catalog.add_book("1984", "George Orwell", 1949)

catalog.display_books()



