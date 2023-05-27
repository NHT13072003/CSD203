class EmptyStackException(Exception):
    pass
#class

class EmptyQueueException(Exception):
    pass
#class

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    #def

#class

#Question 1. Write a program in Python to implement a stack of integer values 
class StackLL:
    def __init__(self):
        self.head = None
        self.tail = None
    #def

    def isEmpty(self):
        return self.head is None
    #def
    
    def clear(self):
        self.head = None
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
            raise EmptyStackException("Stack is empty")
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

    def top(self):
        if self.isEmpty() is True:
            raise EmptyStackException("Stack is empty")
        else:
            return self.tail.data
    #def

    def traversal(self):
        result = []
        curr  = self.head
        if self.isEmpty() is True:
            raise EmptyStackException("Stack is empty")
        else:
            while curr is not None:
                result.append(curr.data)
                curr = curr.next 
            print(result)
    #def

def decimal_to_binary1(decimal_num):
    stack = StackLL()
    if decimal_num == 0:
        stack.push(0)

    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.push(remainder)
        decimal_num //= 2

    binary_num = ""
    while not stack.isEmpty():
        binary_num += str(stack.pop())

    return binary_num
#def

class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None
    #def

    def isEmpty(self):
        return self.head is None
    #def

    def clear(self):
        self.head = None
        self.tail = None

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
            raise EmptyQueueException("Queue is empty")
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

    def first(self):
        if self.isEmpty() is True:
            raise EmptyQueueException("Queue is empty")
        else:
            return self.tail.data
    #def

    def traversal(self):
        result = []
        curr = self.head
        if self.isEmpty() is True:
            raise EmptyQueueException("Queue is empty")
        else:
            while curr is not None:
                result.append(curr.data)
                curr = curr.next
            return result
    #def

def decimal_to_binary2(decimal_num):
    queue = QueueLL()

    while decimal_num > 0:
        decimal_num *= 2
        digit = int(decimal_num)
        queue.enqueue(digit)
        decimal_num -= digit

    binary_num = ""
    while not queue.isEmpty():
        binary_num += str(queue.dequeue())

    return binary_num
#def

