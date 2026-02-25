# Class Definition
class BookStore:

    # Class variable
    NoOfBooks = 0

    # Constructor
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author

        # Increment class variable whenever new object is created
        BookStore.NoOfBooks += 1

    # Instance method
    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")


# Example Usage
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()     # No of books: 1

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()     # No of books: 2

Obj3 = BookStore("Clean Code", "Robert C. Martin")
Obj3.Display()     # No of books: 3