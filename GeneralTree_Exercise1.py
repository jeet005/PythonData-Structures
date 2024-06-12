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

    def print(self, level):
        if level >= self.get_level():
            spaces = '  ' * self.get_level() * 2
            print(spaces + self.data)
            if self.children:
                for child in self.children:
                    child.print(level)


gujrat = TreeNode("Gujrat")
gujrat.add_child(TreeNode("Ahmedabad"))
gujrat.add_child(TreeNode("Baroda"))

karnataka = TreeNode("Karnataka")
karnataka.add_child(TreeNode("Bangalore"))
karnataka.add_child(TreeNode("Mysore"))

newJersy = TreeNode("New Jersey")
newJersy.add_child(TreeNode("Princeton"))
newJersy.add_child(TreeNode("Trenton"))

california = TreeNode("California")
california.add_child(TreeNode("San Francisco"))
california.add_child(TreeNode("Mountain View"))
california.add_child(TreeNode("Palo Alto"))

gg = TreeNode("Global")
india = TreeNode("India")
usa = TreeNode("USA")
india.add_child(gujrat)
india.add_child(karnataka)
usa.add_child(newJersy)
usa.add_child(california)

gg.add_child(india)
gg.add_child(usa)

gg.print(4)
