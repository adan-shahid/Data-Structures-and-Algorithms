# In this circular Linked list, The next of last node points to the head 

# Creating a 4 Node circular linked list

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

head = Node(10)
head.next = Node(5)
head.next.next = Node(20)
head.next.next.next = Node(15)
head.next.next.next.next = head
