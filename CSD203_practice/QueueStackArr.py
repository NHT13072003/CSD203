class QueueArr:
    def __init__(self):
        self.Q = []
    #def

    def isEmpty(self):
        if len(self.Q) == 0:
            return True
    #def

    def enQueue(self,data):
        self.Q.insert(0, data)
    #def 

    def deQueue(self):
        if self.isEmpty() is True:
            return "Queue is Empty, cannot dequeue"
        else:
            self.Q.pop()
        return self.Q
    #def

    def peek(self):
        if self.isEmpty() is True:
            return "Queue is Empty"
        else:
            print("First element of Queue is: "+ str(self.Q[-1]))
    #def

    def size(self):
        return len(self.Q)
    #def

    def traversal(self):
        return self.Q
    #def

#class

# q = QueueArr()
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


class StackArr:
    def __init__(self):
        self.S = []
    #def

    def isEmpty(self):
        if len(self.Q) == 0:
            return True
    #def

    def push(self,data):
        self.S.append(data)
    #def

    def pop(self):
        self.S.pop()
    #def

    def peek(self):
        if self.isEmpty is True:
            return "Stack is Empty"
        else:
            print("First element of Stack is: "+ str(self.S[-1]))
    #def

    def size(self):
        return len(self.S)
    #def

    def traversal(self):
        return self.S
    #def

#class

# s = StackArr()
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
    