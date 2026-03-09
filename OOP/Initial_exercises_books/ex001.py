"""
Create a Book class following attributtes:
- Title
- Author
- Pages
- A showInfo() method to display all informations about a book
Then, create 2 books.
"""
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nTotal pages: {self.pages}\n")

book1 = Book("Clean Code", "Robert C. Martin", 425)
book2 = Book("Think Python", "Allen B. Downey", 292)

print("Show books informations")
print("-"*20)

book1.show_info()
book2.show_info()
        