class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level

    def print(self):
        spaces = ' ' * self.get_level()
        print(spaces + self.data)
        if self.children:
            for child in self.children:
                child.print()

root = TreeNode("Electronics")


laptop = TreeNode("laptop")

laptop.add_child(TreeNode('Dell'))
laptop.add_child(TreeNode('Mac'))
laptop.add_child(TreeNode('HP'))

mobile = TreeNode("Mobile")

mobile.add_child(TreeNode('iphone'))
mobile.add_child(TreeNode('vivo'))
mobile.add_child(TreeNode('samsung'))

tv = TreeNode("TV")

tv.add_child(TreeNode('LG'))
tv.add_child(TreeNode('Xiomi'))
tv.add_child(TreeNode('panasonic'))

root.add_child(laptop)
root.add_child(mobile)
root.add_child(tv)

root.print()
print(tv.get_level())