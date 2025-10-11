"""
EXERCISE 1: Basic Class Creation
Create a Book class that has:
- Attributes: title, author, pages
- Methods: get_info() that returns a string with book information
"""



class Book():
    def __init__(self,title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"the title of the book is {self.title} and the author is {self.author} and the n.of pages are {self.pages}"

book1 = Book("Python 101", "John Doe", 300)
#print(Book.get_info())
print(book1.get_info())