class Book:
    """
    Base class for all books in the library.
    """
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class EBook(Book):
    """
    Represents an electronic book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size # File size in KB

class PrintBook(Book):
    """
    Represents a physical print book, inheriting from Book.
    """
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """
    Manages a collection of books (Book, EBook, and PrintBook instances).
    Demonstrates composition.
    """
    def __init__(self):
        self.books = [] # A list to store various types of book objects

    def add_book(self, book: Book):
        """
        Adds a book instance to the library's collection.

        Args:
            book: An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            elif isinstance(book, Book): # This condition will catch general Book instances
                print(f"Book: {book.title} by {book.author}")

# --- Main execution logic ---
if __name__ == "__main__":
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()