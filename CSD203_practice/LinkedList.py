class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    #def

#class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    #def

    def isEmpty(self):
        return self.head is None
    #def

    def addFirst(self,data):
        newnode = Node(data)
        if self.isEmpty() == True:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head =newnode
    #def

    def addLast(self,data):
        newnode = Node(data)
        if self.isEmpty() == True:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
    #def

    def add(self,index,data):
        newnode = Node(data)
        count = 1
        curr = self.head
        while count != index:
            count +=1
            curr = curr.next
            if curr is None and count != index:
                print("Do not have index you want to add.")
                break
        newnode.next = curr.next
        curr.next = newnode
    #def

    def removeFirst(self):
        temp = self.head
        if self.isEmpty ==True:
            return 'LinkedList is Empty'
        else:
            self.head = self.head.next
            del temp
    #def

    def removeLast(self):
        if self.isEmpty():
            return 'LinkedList is Empty'
        elif self.head == self.tail:
            curr = self.head
            self.head = None
            self.tail = None
            del curr
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            temp = curr.next
            self.tail = curr
            self.tail.next = None
            del temp
    #def

    def removeData(self,data):
        
        if self.isEmpty ==True:
            return None
        elif self.head.data == data:
            curr = self.head
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                self.head.next = self.head
                curr.next = None
                del curr
        elif self.tail.data == data:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            del curr.next
            self.tail = curr
        else:
            curr = self.head
            while curr.next.data != data:
                curr = curr.next
                if curr.next == self.tail:
                    print("Do not have data you want to remove.")
                    break
                if curr.next.data == data:
                    temp = curr.next
                    curr.next = curr.next.next
                    del temp
                    break
    #def

    def removeIndex(self,index):
        if self.isEmpty():
            return 'LinkedList is Empty'
        elif index < 1:
            return 'Invalid index'
        elif index == 1:
            return self.removeFirst()
        else:
            count = 1
            curr = self.head
            while count != index:
                if count == index-1:
                    temp = curr.next
                    curr.next = curr.next.next
                    temp.next = None
                    del temp
                    break
                count +=1
                curr = curr.next
                if curr.next == self.tail and count != index:
                    print("Do not have index you want to remove")
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
ll = LinkedList()
ll.addFirst(3)
ll.addFirst(2)
ll.addFirst(1)
ll.addLast(6)
ll.addLast(7)
ll.add(3,4)
ll.add(4,5)
ll.traversal()
ll.removeFirst()
ll.traversal()
ll.removeLast()
ll.traversal()
ll.removeData(4)
ll.removeData(7)
ll.traversal()
ll.removeIndex(2)
ll.traversal()
ll.removeIndex(6)
ll.traversal()
