from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)

    def pop(self): #pop the last element
        return self.container.pop()

    def peek(self): #this method will return the last element, not delete the last element
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    def reverse_string(self, val):
        return val[::-1]        

ss = Stack()
print(ss.reverse_string('Hello world'))
