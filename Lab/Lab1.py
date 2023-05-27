#Question 1.
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

    def addToHead(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    #def

    def addToTail(self,x):
        newNode = Node(x)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    #def

    def addAfter(self,p,x):
        newNode = Node(x)
        newNode.next = p.next
        p.next = newNode
    #def

    def traverse(self):
        if self.isEmpty():
            return "Linked List is empty!"
        else:
            currNode = self.head
            while currNode:
                print(currNode.data, end=" ")
                currNode = currNode.next
            print()
    #def

    def deleteFromHead(self):
        if self.isEmpty():
            return "Linked List is empty!"
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            self.head = self.head.next
            return f"Deleted the element {temp.data}"
    #def

    def deleteFromTail(self):
        if self.isEmpty():
            return "Linked List is empty!"
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return f"Deleted the element {temp.data}"
        elif self.head.next == self.tail:
            temp = self.tail
            self.head.next = None
            return f"Deleted the element {temp.data}"
        else:
            curr = self.head
            while curr.next.next:
                curr = curr.next
            temp = curr.next
            curr.next = None
            self.tail = curr
            return f"Deleted the element {temp.data}"
    #def

    def deleteAfter(self,p):
        if p.next is None:
            return f"Do not have element after node{p.data}"
        else:
            temp = p.next
            p.next = p.next.next
            return f"Deleted the element {temp.data} after node {p.data}"
    #def
    
    def delete(self,x):
        if self.isEmpty():
            return "Linked List is empty"
        elif self.head.data == x:
            self.head = self.head.next
            return f"Deleted element {x}"
        else:
            curr = self.head
            while curr.next is not None and curr.next.data != x:
                curr = curr.next
            if curr.next is None and curr.next.data != x:
                return f"Linked List do not have element {x}"
            else:
                curr.next = curr.next.next
                return f"Deleted element {x}"
    #def 

    def search(self,x):
        if self.isEmpty():
            return "Linked List is empty"
        elif self.head.data == x:
            return f"Element {x} in the first node"
        else:
            curr = self.head
            while curr.next and curr.next.data != x:
                curr = curr.next
            if curr.next is None and curr.next.data != x:
                return f"Can not search element {x}"
            else:
                return f"Elemet {x} after element {curr.data}"
    #def

    def count(self):
        count = 0
        curr = self.head
        while curr:
            count +=1
            curr = curr.next
        return count
    #def

    def deletedeleteAt(self,i):
        if self.isEmpty():
            return "Linked List is empty"
        elif i == 0:
            self.head == self.head.next
            return 'Deleted the first element'
        else:
            if i > self.count() -1:
                return 'Index out of range'
            else:
                curr = self.head
                for j in range(i-1):
                    curr = curr.next
                curr.next = curr.next.next
                return f"Deleted the {i}-th element "
    #def

    def sort(self):
        if self.isEmpty():
            return "Linked List is empty"
        curr = self.head
        while curr:
            next = curr.next
            while next:
                if curr.data > next.data:
                    curr.data, next.data = next.data, curr.data
                next = next.next
            curr = curr.next
        return "Sorted the Linked List"
    #def

    def deleteNode(self,p):
        if self.isEmpty():
            return "Linked List is empty"
        elif self.head == p:
            self.head = self.head.next
        else:
            curr = self.head
            while curr.next != p:
                curr = curr.next
                if curr == self.tail and curr != p:
                    return f'Node {p.data} out of linked list'
                else:
                    curr.next = curr.next.next
                    return f'Deleted node {p.data}'
    #def

    def toArray(self):
        if self.isEmpty():
            return "Linked List is empty!"
        else:
            result = []
            curr = self.head
            while curr is not None:
                result.append(curr.data)
                curr = curr.next
            return result
    #def
    
    def merge(self, other):
        result = LinkedList()
        current1 = self.head
        current2 = other.head
        while current1 != None and current2 != None:
            if current1.val < current2.val:
                result.addToTail(current1.val)
                current1 = current1.next
            else:
                result.addToTail(current2.val)
                current2 = current2.next
        while current1 != None:
            result.addToTail(current1.val)
            current1 = current1.next
        while current2 != None:
            result.addToTail(current2.val)
            current2 = current2.next
        return result  
    #def
    
    def addBefore(self,p,x):
        if p is None or self.head is None:
            return
        if p == self.head:
            new_node = Node(x)
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next != p:
            current = current.next

        if current.next == p:
            new_node = Node(x)
            new_node.next = p
            current.next = new_node
    #def

    def attachLinkedList(self, list2):
        if self.head is None:
            self.head = list2.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = list2.head
    #def

    def max(self):
        if self.head is None:
            return None
        
        max_value = self.head.data
        current = self.head.next
        
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        
        return max_value
    #def

    def min(self):
        if self.head is None:
            return None
        
        min_value = self.head.data
        current = self.head.next
        
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        
        return min_value
    #def

    def sum(self):
        total = 0
        current = self.head

        while current:
            total += current.data
            current = current.next

        return total
    #def

    def avg(self):
        if self.head is None:
            return None

        total = 0
        count = 0
        current = self.head

        while current:
            total += current.data
            count += 1
            current = current.next

        return total / count
    #def

    def sorted(self):
        if self.head is None or self.head.next is None:
            return True

        current = self.head
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next

        return True
    #def

    def insert(self, x):
        new_node = Node(x)

        if self.head is None:
            self.head = new_node
            return

        if x < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < x:
            current = current.next

        new_node.next = current.next
        current.next = new_node
    #def

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
    #def

    def sameContents(self, list2):
        current1 = self.head
        current2 = list2.head

        while current1 and current2:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next

        # If both lists have the same number of nodes
        # and the contents of all nodes match, return True.
        # Otherwise, return False.
        return current1 is None and current2 is None
    #def





        
