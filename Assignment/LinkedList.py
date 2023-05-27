from tabulate import tabulate
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
        current = self.head
        book_data = []
        
        while current:
            book = current.data
            book_data.append([book.bid, book.title, book.author, book.status])
            current = current.next
        
        headers = ["Book ID", "Title", "Author", "Status"]
        print(tabulate(book_data, headers, tablefmt="grid"))


