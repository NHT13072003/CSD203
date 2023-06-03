class Book:
    def __init__(self, bid, title, author, status):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status
    #def

#class

def add_book(books_list):
    bid = input("Enter the book ID: ")
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    status = "available"
    check_book = books_list.search(bid)
    if check_book is None:
        book = Book(bid, title, author, status)
        books_list.insert(book)
        print("Book added successfully.")
        books_list.writetxt()
    else:
        print("Book add to failure because already exist.")
    #if/else Check available book
#def