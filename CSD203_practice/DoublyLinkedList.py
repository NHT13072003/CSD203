class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    #def

#class

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    #def

    def isEmpty(self):
        return self.head is None
    #def

    def addFirst(self,data):
        newnode = Node(data)
        if self.isEmpty():
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
    #def

    def addLast(self,data):
        newnode = Node(data)
        if self.isEmpty():
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
    #def

    def add(self,index,data):
        newnode = Node(data)
        if self.isEmpty():
            return "Can not add with your index because Doubly Linked List is empty"
        else:
            count = 1
            curr = self.head
            while count != index and curr.next is not None:
                count +=1
                curr = curr.next
                if curr is None and count != index:
                    print("Do not have index you want to add.")
                    break
            curr.next.prev =newnode
            newnode.next = curr.next
            curr.next = newnode
            newnode.prev = curr
    #def

    def removeFirst(self):
        if self.isEmpty():
            return "Doubly Linked List is empty"
        else:
            curr = self.head
            self.head = self.head.next
            self.head.prev = None
            curr.next = None
            del curr
    #def

    def removeLast(self):
        if self.isEmpty():
            return "Doubly Linked List is empty"
        else:
            curr = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            curr.prev = None
            del curr
    #def

    def removeIndex(self,index):
        if self.isEmpty():
            return "Doubly Linked List is empty"
        else:
            count = 1
            curr = self.head
            while count != index:
                count += 1
                curr = curr.next
                if curr is None and count != index:
                    print("Do not have index you want to remove.")
                    break
                if count == index: 
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    curr.next = None
                    curr.prev = None
                    del curr
                    break

    #def

    def removeData(self,data):
        if self.isEmpty():
            return "Doubly Linked List is empty"
        elif self.head.data == data:
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                curr = self.head
                self.head.next = self.head
                self.head.prev = None
                curr.next = None
                del curr
        elif self.tail.data == data:
            curr = self.tail
            self.tail.prev = self.tail
            self.tail.next = None
            curr.prev = None
            del curr
        else:
            curr = self.head
            while curr.data != data: 
                curr = curr.next 
                if curr.data == data:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    curr.prev = None
                    curr.next = None
                    del curr
                    break 
                if curr == self.tail and curr.data != data:
                    print("Do not have data you want to remove.")
                    break           
    #def

    def traversal(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        print(result)
    #def

#class
ll = DoublyLinkedList()
ll.addFirst(3)
ll.addFirst(2)
ll.addFirst(1)
ll.addLast(6)
ll.addLast(7)
ll.add(3,4)
ll.add(4,5)
ll.traversal()##
ll.removeFirst()
ll.traversal()##
ll.removeLast()
ll.traversal()##
ll.removeData(3)
ll.removeData(7)
ll.traversal()##
ll.removeIndex(2)
ll.traversal()
ll.removeIndex(6)
ll.traversal()