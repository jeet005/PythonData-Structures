class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):

        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next
    
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr.next:
            count += 1
            itr = itr.next
        print(count)
    
    def remove(self, data):
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
    
    def remove_at_index(self, index):
        if index < 0:
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.remove_at_index(2)
ll.print()
# ll.get_length()