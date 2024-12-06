# In Doubly Linked List, we have refernece to both 
# previous and next Node
## Previous of head is None and
## next of last node is None

class Node:
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None

# Traverse through the DLL
    def printList(head):
        curr = head
        while curr != None:
            print(curr.key, end = " ")
            curr = curr.next

# Insertion at the Beginning of Doubly Linked List
    def insertBegin(head,x):
        temp = Node(x)
        if head != None:
            head.prev = temp
        temp.next = head
        return temp
    
# Insert at the End of DLL

    def insertEnd(head,x):
        temp = Node(x)
        if head == None:
            return temp
        else:
            curr = head
            while curr.next != None:
                curr = curr.next
            curr.next = temp
            temp.prev = curr
            return head

# Delete the Head of DLL

    def delHead(head):
            if head == None:
                return None
            if head.next == None:
                return None
            else:
                head = head.next
                head.prev = None
                return head
            
# Delete the Last Node of DLL

    def delLast(head):
        if head == None:
            return None
        if head.next == None:
            return None
        curr = head
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        return head
    
# Reverse a Doubly Linked List

    def reverseDll(head):
        if head == None:
            return None
        if head.next == None:
            return head
        curr = head
        prev = None
        while curr != None:
            prev = curr
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev
        return prev











# Here I am creating Simple 3 Node Circular Linked List
head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head

temp1.next = temp2
temp2.prev = temp1