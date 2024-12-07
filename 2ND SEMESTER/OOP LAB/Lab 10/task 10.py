class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
class Book(Document):
    def __init__(self, title, author, genre="Unknown", pages=0):
        super().__init__(title, author)
        self.genre = genre
        self.pages = pages
    def display_info(self):
        super().display_info()  # Call the parent class method
        print(f"Genre: {self.genre}")
        print(f"Pages: {self.pages}")
    @classmethod
    def from_title_author(cls, title, author):
        # Alternative constructor with just title and author
        return cls(title, author)

    @classmethod
    def from_full_info(cls, title, author, genre, pages):
        # Alternative constructor with title, author, genre, and pages
        return cls(title, author, genre, pages)
class Article(Document):
    def __init__(self, title, author, journal="Unknown", doi="Not Available"):
        super().__init__(title, author)
        self.journal = journal
        self.doi = doi
    def display_info(self):
        super().display_info()  # Call the parent class method
        print(f"Journal: {self.journal}")
        print(f"DOI: {self.doi}")
    @classmethod
    def from_title_author(cls, title, author):
        # Alternative constructor with just title and author
        return cls(title, author)

    @classmethod
    def from_full_info(cls, title, author, journal, doi):
        # Alternative constructor with title, author, journal, and DOI
        return cls(title, author, journal, doi)
book1 = Book.from_full_info("To Kill a Mockingbird", "Harper Lee", "Fiction", 281)

# Book created using the title and author only
book2 = Book.from_title_author("1984", "George Orwell")

# Article created using the full initialization
article1 = Article.from_full_info("Research on AI", "John Doe", "AI Journal", "10.1000/abcd1234")

# Article created using the title and author only
article2 = Article.from_title_author("Quantum Computing", "Jane Smith")

# Displaying the information of the book and article
print("Book Info (Full):")
book1.display_info()

print("\nBook Info (Title and Author Only):")
book2.display_info()

print("\nArticle Info (Full):")
article1.display_info()

print("\nArticle Info (Title and Author Only):")
article2.display_info()