class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        print("Book:", self.title)
        print("Author:", self.author)


b1 = Book("Python Basics", "John")
b1.show()