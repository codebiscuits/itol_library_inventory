class Book:
    def __init__(self, title: str, author: str, avaliable: bool=True) -> None:
        self.title = title
        self.author = author
        self.avaliable = avaliable

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book: Book) -> None:
        self.books.append(new_book)

    def search_by_title(self, title: str) -> None:
        # result = [book for book in self.books if book.title.lower() == title.lower()]
        result = list(filter(lambda book: book.title.lower() == title.lower(), self.books))
        print(f"\nWe have {len(result)} book with the title \'{title}\':")
        for title in result:
            print(f"- {title.title} by {title.author}")

    def search_by_author(self, author: str) -> None:
        result = [book for book in self.books if book.author.lower() == author.lower()]
        print(f"\nWe have {len(result)} books by {author}:")
        for title in result:
            print(f"- {title.title}")

    def update_availability(self, title, available) -> None:
        for book in self.books:
            if book.title.lower() == title.lower():
                book.avaliable = available
                print(f"\n{book.title} by {book.author} is now {"available" if available else "unavailable"}.")

    def check_availability(self, title) -> None:
        result = [book for book in self.books if book.title.lower() == title.lower()]
        print(f"\nChecking availability for \'{title}\':")
        for title in result:
            print(f"- {title.title} by {title.author} is {"available" if title.avaliable else "Unavailable"})")

library = Library()

library.add_book(Book("Magician", "Raymond E Feist", True))
library.add_book(Book("Harry Potter and The Philosopher's Stone", "JK Rowling", True))
library.add_book(Book("Do Androids Dream of Electric Sheep?", "Philip K Dick", True))
library.add_book(Book("Martian Time Slip", "Philip K Dick", True))

print("\nAll books:")
for book in library.books:
    print(f"{book.title:<50}{book.author:<20}{"Available" if book.avaliable else "Unavailable"}")

library.search_by_title("Magician")

library.search_by_author("Philip K Dick")

library.check_availability("Martian Time Slip")

library.update_availability("Magician", False)

print("\nAll books:")
for book in library.books:
    print(f"{book.title:<50}{book.author:<20}{"Available" if book.avaliable else "Not available"}")
