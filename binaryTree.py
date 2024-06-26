class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, val):
        if val < self.data:
            #add value in left
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinarySearchTree(val)
        elif val > self.data:
            #add value in right
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinarySearchTree(val)
            
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        
        while self.left:
            self = self.left
        
        return self.data

    def find_max(self):
        
        while self.right:
            self = self.right
        
        return self.data

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
            
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
        
        return self
    

def build_tree(elements):
    
    root = BinarySearchTree(elements[0])

    for x in range(1, len(elements)):
        root.add_child(elements[x])

    return root

elements = [17, 4, 1, 20, 9, 23, 18, 34]
root = build_tree(elements)
print(root.in_order_traversal())
print(root.search(20))
print(root.find_min())
print(root.find_max())
root.delete(20)
root.delete(1)
print(root.in_order_traversal())


            