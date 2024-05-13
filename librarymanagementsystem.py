class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self):
        n = int(input("Enter the number of books you want to add: "))
        print(f"Enter the titles of the {n} books:")
        for _ in range(n):
            a = input()
            self.books.append(a)
        self.no_of_books += n  

    def show_books(self):
        print(f"The library has {self.no_of_books} books.")
        if self.books:
            print("Books available in the library:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")


lib = Library()
lib.add_book()  
lib.show_books()  
