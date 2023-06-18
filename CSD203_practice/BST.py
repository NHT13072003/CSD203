class Node:
    def __init__(self, data = None):
        self.data = data
        self.rt = None
        self.lt = None
    #def
    # Đối với BST function insert nên để ở class node. Đoán thế đã code mới biết được

    def insert(self, data):
        if self is None:
            self.root = Node(data)
        elif data < self.data:
            if self.lt == None:
                self.lt = Node(data)
            else:
                self.lt.insert(data)
        elif data > self.data:
            if self.rt == None:
                self.rt = Node(data)
            else:
                self.rt.insert(data)
        else:
            print(f"Duplicate data {data}")
    #def

#class

class BinarySearchTree:
    def __init__(self, data = None):
        if data == None:
            self.root = None
        else: 
            self.root = Node(data)
    #def

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.root.insert(data)
    #def

    def remove(self, data):
        pass
    #def

    def preOrder(self, key = 0):
        curr = key
        if key == 0:
            curr = self.root
        if key == None:
            return []
        else:
            result =[]
            result.append(curr.data)
            result_lt = self.preOrder(curr.lt)
            for x in result_lt:
                result.append(x)
            result_rt = self.preOrder(curr.rt)
            for x in result_rt:
                result.append(x)
        
        return result

L = [100,20,200,10,30,150,300]
tree = BinarySearchTree()
for x in L:
    tree.insert(x)
preOrder = tree.preOrder()
print('1', preOrder)