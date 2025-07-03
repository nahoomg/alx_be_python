# book_class.py

class Book:
    """
    A class to represent a book, demonstrating Python's magic methods.
    """

    def __init__(self, title, author, year):
        """
        Constructor method to initialize a Book instance.
        """
        self.title = title
        self.author = author
        self.year = year
        # print(f"Book '{self.title}' created.") # Optional: can remove this print if not explicitly asked

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an unambiguous, developer-friendly string representation of the Book object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """
        Destructor method, called when the object is about to be destroyed.
        """
        print(f"Deleting {self.title}")