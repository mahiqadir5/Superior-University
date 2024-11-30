class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}"

class Book(Document):
    def __init__(self, title, author, genre="unknown", pages=0):
        super().__init__(title, author) 
        self.genre = genre
        self.pages = pages

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}\nGenre: {self.genre}\nPages: {self.pages}"

class Article(Document):
    def __init__(self, title, author, journal="unknown", DOI="unknown"):
        super().__init__(title, author) 
        self.journal = journal
        self.DOI = DOI

    def display_info(self):
        info = super().display_info()
        return f"{info}\nJournal: {self.journal}\nDOI: {self.DOI}"


book1 = Book("Python Basics", "John Doe")
print(book1.display_info())
print()

book2 = Book("Advanced Python", "Jane Smith", "Programming", 300)
print(book2.display_info())
print()

article1 = Article("AI in Healthcare", "Dr. Alice")
print(article1.display_info())
print()

article2 = Article("Quantum Computing", "Dr. Bob", "Science Journal", "mahi/012")
print(article2.display_info()) 

with open('documents.txt', 'w') as file:
    # Writing Book data to text file
    file.write("Book 1:\n")
    file.write(book1.display_info())
    file.write("\n\n")

    file.write("Book 2:\n")
    file.write(book2.display_info())
    file.write("\n\n")

    # Writing Article data to text file
    file.write("Article 1:\n")
    file.write(article1.display_info())
    file.write("\n\n")

    file.write("Article 2:\n")
    file.write(article2.display_info())
    file.write("\n\n")

print("Data has been written to 'documents.txt'")