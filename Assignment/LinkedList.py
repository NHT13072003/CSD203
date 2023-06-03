from tabulate import tabulate
from AddBook import *
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, bid):
        current = self.head
        while current:
            if current.data.bid == bid:
                return current.data
            current = current.next
        return None

    def delete(self, bid):
        if self.head is None:
            return

        if self.head.data.bid == bid:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current:
            if current.data.bid == bid:
                prev.next = current.next
                return
            prev = current
            current = current.next
    def display(self):
        filename = "book_data.txt"
        with open(filename, 'r') as file:
            content = file.read()
        print(content)
        # current = self.head
        # book_data = []
        
        # while current:
        #     book = current.data
        #     book_data.append([book.bid, book.title, book.author, book.status])
        #     current = current.next
        
        # headers = ["Book ID", "Title", "Author", "Status"]
        # print(tabulate(book_data, headers, tablefmt="grid"))
    
    #edit
    def writetxt(self):
        current = self.head
        book_data = []
        
        while current:
            book = current.data
            book_data.append([book.bid, book.title, book.author, book.status])
            current = current.next
        
        headers = ["Book ID", "Title", "Author", "Status"]
        table_str = tabulate(book_data, headers, tablefmt="grid")
        with open("book_data.txt", "w") as file:
            file.write(table_str)
    #def

def restoreLL(filename):
    books_list = LinkedList()  # Create LinkedList object outside the loop
    
    with open(filename, "r") as file:
        table_str = file.read()
        lines = table_str.split('\n')
        headers = lines[1].split('|')[1:-1]
        for line in lines[3:-1:2]:
            data = line.split('|')[1:-1]
            book = Book(data[0], data[1], data[2], data[3])
            books_list.insert(book)  # Insert the book into the existing LinkedList object
        
    return books_list
#def
