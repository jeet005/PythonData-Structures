class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):

        if data == self.data:
            return

        if data < self.data:

            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        
        elements = []

        # visiting the left node
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements
    
    def search(self, val):
        if val == self.data:
            return True
        
        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        
        return False

    def find_min(self):
        
        while self.left:
            self = self.left
        
        return self.data
    
    def find_max(self):
        
        while self.right:
            self = self.right
        
        return self.data

    def calc_sum(self):

        elements = []

        # visiting the left node
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        
        return sum(elements)



def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for x in range(1, len(elements)):
        root.add_child(elements[x])
    
    return root

elements = [17, 4, 1, 20, 9, 23, 18, 34]
tree = build_tree(elements)
print(tree.in_order_traversal())
print(tree.search(34))
print(tree.find_min())
print(tree.find_max())
print(tree.calc_sum())