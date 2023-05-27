class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    #def

#class

class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None
    #def

    def isEmpty(self):
        return self.head is None
    #def

    def enQueue(self,data):
        newNode = Node(data)
        if self.isEmpty() is True:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    #def

    def deQueue(self):
        if self.isEmpty() is True:
            print("Queue is Empty")
        elif self.head == self.tail:
            popped = self.head
            self.head = None
            self.tail = None
        else:
            popped = self.tail
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
            self.tail = curr
            del popped
    #def

    def peek(self):
        if self.isEmpty() is True:
            print("Queue is Empty")
        else:
            print("First element of Queue is: " + str(self.tail.data))
            return self.tail
    #def

    def traversal(self):
        result = []
        curr = self.head
        if self.isEmpty() is True:
            return 'Queue is Empty'
        else:
            while curr is not None:
                result.append(curr.data)
                curr = curr.next
            return result
    #def

    def size(self):
        if self.isEmpty() is True:
            return 'Queue is Empty'
        else:
            count = 0
            curr = self.head
            while curr is not None:
                count +=1
                curr = curr.next
            return count
    #def

#class

# q = QueueLL()
# q.enQueue(1)
# q.enQueue(2)
# q.enQueue(3)
# q.enQueue(4)
# q.enQueue(5)
# size = q.size()
# print(size)
# result = q.traversal()
# print(result)
# q.deQueue()
# result = q.traversal()
# print(result)
# q.peek()
# result = q.traversal()
# print(result)
# size = q.size()
# print(size)

class StackLL:
    def __init__(self):
        self.head = None
        self.tail = None
    #def

    def isEmpty(self):
        return self.head is None
    #def

    def push(self,data):
        newnode = Node(data)
        if self.isEmpty() is True:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
    #def

    def pop(self):
        
        if self.isEmpty() is True:
            return 'Stack is Empty'
        elif self.head == self.tail:
            popped = self.head
            self.head = None
            self.tail = None
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next
            popped = curr.next
            self.tail = curr
            self.tail.next = None
        del popped
    #def

    def peek(self):
        if self.isEmpty() is True:
            return 'Stack is Empty'
        else:
            print("First element of Stack is: "+ str(self.tail.data))
    #def

    def traversal(self):
        result = []
        curr  = self.head
        if self.isEmpty() is True:
            return 'Stack is Empty'
        else:
            while curr is not None:
                result.append(curr.data)
                curr = curr.next 
            return result
    #def
     
    def size(self):
        if self.isEmpty() is True:
            return 'Stack is Empty'
        else:
            count = 0
            curr = self.head
            while curr is not None:
                count +=1
                curr = curr.next
            return count
    #def

#class

# s = StackLL()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# result = s.traversal()
# print(result)
# size = s.size()
# print(size)
# s.pop()
# result = s.traversal()
# print(result)
# s.peek()
# result = s.traversal()
# print(result)
# size = s.size()
# print(size)
