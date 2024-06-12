class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.designation = designation
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

    def print(self, showtype):
        spaces = '  ' * self.get_level() * 2
        if showtype == 'name':
            print(spaces + self.data)
        elif showtype == 'designation':
            print(spaces + self.designation)
        elif showtype == 'both':
            print(spaces + self.data + '(' + self.designation + ')')
        if self.children:
            for child in self.children:
                child.print(showtype)

ceo = TreeNode("Nilupul", "CEO")
cto = TreeNode("Chinmay", "CTO")
infraHead = TreeNode("Vishwa", "Infrastructure Head")


infraHead.add_child(TreeNode('Dhaval', 'Cloud Manager'))
infraHead.add_child(TreeNode('Abhijit', 'App Manager'))

cto.add_child(TreeNode("Aamir", "Application Head"))

hrhead = TreeNode("Gels", "HR Head")
hrhead.add_child(TreeNode("Peter", "Recruitment Manager"))
hrhead.add_child(TreeNode("Waqas", "Policy Manager"))

ceo.add_child(cto)
cto.add_child(infraHead)
ceo.add_child(hrhead)

ceo.print('both')