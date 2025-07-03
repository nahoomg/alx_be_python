# book_class.py

class Book:
    """
    A class to represent a book, demonstrating Python's magic methods.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Constructor method to initialize a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.") # Optional: to show when __init__ is called

    def __str__(self) -> str:
        """
        Returns a user-friendly string representation of the Book object.
        This is what gets printed by `print(book_object)`.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """
        Returns an unambiguous, developer-friendly string representation of the Book object.
        This string should ideally be able to recreate the object.
        This is what gets printed by `repr(book_object)`.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor method, called when the object is about to be destroyed (deleted).
        Note: The exact timing of __del__ calls can be unpredictable due to garbage collection.
        """
        print(f"Deleting {self.title}")