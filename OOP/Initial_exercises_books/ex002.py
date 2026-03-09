"""
Same thing as exercise ex001.py, but now the Book class 
has a class attribute and a new logical method.
"""
class Book:
    category = "Programming"

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_book_short(self):
        return self.pages >= 300
            
    def show_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nTotal pages: {self.pages}\nCategory: {self.category}\nIs short: {self.is_book_short()}\n")
    
book1 = Book("Clean Code", "Robert C. Martin", 425)
book2 = Book("Think Python", "Allen B. Downey", 292)

print("Show books informations")
print("-"*20)

book1.show_info()
book2.show_info()
