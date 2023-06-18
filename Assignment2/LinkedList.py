from Customer import *
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

    def search(self,key):
        current = self.head

        while current:
            if current.data.key == key:
                return current.data
            current = current.next
        return None

    def delete(self, ccode):
        if self.head is None:
            return None
        if ccode == self.head.data.ccode:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while True:
            if current.data.ccode == ccode:
                prev.next = current.next
                return
            prev = current
            current = current.next


    def display(filename):
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
    def txtCustomer(self):
        current = self.head
        result = []
        
        while current:
            cus = current.data
            result.append([cus.ccode, cus.cname, cus.phone])
            current = current.next
        
        headers = ["Customer Code", "Customer Name", "Phone number"]
        table_str = tabulate(result, headers, tablefmt="grid")
        with open("Customer_List.txt", "w") as file:
            file.write(table_str)
    #def

    def txtOrder(self):
        current = self.head
        result = []
        
        while current:
            order = current.data
            result.append([order.pcode, order.ccode, order.quantity])
            current = current.next
        
        headers = ["Product Code", "Customer Code", "Product Quantity"]
        table_str = tabulate(result, headers, tablefmt="grid")
        with open("Order_List.txt", "w") as file:
            file.write(table_str)
    #def
    
def loadLL(filename):
    cList = LinkedList()
    with open(filename, "r") as file:
        table_str = file.read()
        lines = table_str.split('\n')
        for line in lines[3:-1:2]:
            data = line.split('|')[1:-1]  
            customer = Customer(data[0].strip(), data[1].strip(), data[2].strip())  
            cList.insert(customer)
#def
