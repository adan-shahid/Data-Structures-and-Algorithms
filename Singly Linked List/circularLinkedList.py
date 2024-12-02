# In this circular Linked list, The next of last node points to the head 

# Creating a 4 Node circular linked list

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

# Circular Linked List Traversal--> printing the whole list

    def printCircular(head):    #
        if head == None:
            return
        print(head.key, end = " ")
        curr = head.next
        while curr != head:
            print(curr.key, end = " ")
            curr = curr.next


# Insert at the beginnning of Circular Linked List

    # Linear Time

    def insertBeg1(head,x):
        temp = Node(x)
        if head == None:
            temp.next = temp
            return temp
        curr = head
        while curr.next != head:
            curr = curr.next
        curr.next = temp
        temp.next = head
        return temp

    # Constant Time --> idea is to insert at the second position and them swap the key with first node

    def insertBeg2(head,x):
        temp = Node(x)
        if head == None:
            temp.next = temp
            return temp
        else:
            temp.next = head.next
            head.next = temp
            head.key, temp.key = temp.key, head.key
            return head


# Insert at the End of Circular Linked List

        # Naive approach

    def insertEnd1(head,x):
        temp = Node(x)
        if head == None:
            temp.next = temp
            return temp
        else:
            curr = head
            while curr.next != head:
                curr = curr.next
            curr.next = temp
            temp.next = head
            return head



        # Efficient Approach

    def insertEnd2(head,x):
        temp = Node(x)
        if head == None:
            temp.next = temp
            return temp
        else:
            temp.next = head.next
            head.next = temp
            temp.key, head.key = head.key, temp.key
            return temp


head = Node(10)
head.next = Node(5)
head.next.next = Node(20)
head.next.next.next = Node(15)
head.next.next.next.next = head

Node.insertEnd2(head,2)
Node.printCircular(head)
