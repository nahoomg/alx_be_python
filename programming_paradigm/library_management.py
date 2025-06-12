class Book:
    """
    Represents a book in the library with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Book title cannot be empty.")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Book author cannot be empty.")

        self.title = title
        self.author = author
        self._is_checked_out = False # Private attribute to track availability

    def check_out(self):
        """
        Marks the book as checked out if it's currently available.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """
        Marks the book as available if it's currently checked out.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """
        Checks if the book is currently available.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of books in the library.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = [] # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added to the library.")
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book by its title.

        Args:
            title (str): The title of the book to check out.

        Returns:
            bool: True if the book was found and successfully checked out, False otherwise.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """
        Returns a book by its title.

        Args:
            title (str): The title of the book to return.

        Returns:
            bool: True if the book was found and successfully returned, False otherwise.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """
        Lists all available books in the library.
        """
        available_found = False
        for book in self._books:
            if book.is_available():
                print(book)
                available_found = True
        if not available_found and not self._books:
            print("The library is empty.")
        elif not available_found:
            print("No books are currently available.")