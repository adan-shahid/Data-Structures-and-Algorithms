# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Simple Linked List implementation in Python.

## Head is basically Reference to the First Node. ##


class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
    
        
# Traversing through a  linked list

    def printlist(head):
        curr = head
        while curr != None:
            print(curr.key, end = ' ')
            curr = curr.next
            
# Search in a Linked List

    def search(head, x):
        curr = head
        pos = 1
        while curr != None:
            if curr.key == x:
                print("\n",pos)
            pos = pos + 1
            curr = curr.next
        return -1
    
# Insert at the beginning of the singly linked list

    def insertBegin(head, key):
        temp = Node(key)
        temp.next = head
        return temp
    
# Insert at the end of the singly linked list
    
    def insertEnd(head, key):
        if head == None:
            return Node(key)
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = Node(key)
        return head
    
# Insert at any given position in the singly linked list

    def insertPos(head, data, pos):
        temp = Node(data)
        if pos == 1:
            temp.next = head
            return temp
        
        curr = head
        for i in range(pos - 2):
            curr = curr.next
            if curr == None:
                return head
            
        temp.next = curr.next  #this should written first and
        curr.next = temp       # then this line.
        return head
        
# Delete the first Node of Singly Linked List

    def delFirst(head):
        if head == None:
            return None
        else:
            return head.next
        
# Delete Last Node of the Singly Linked List

    def delLast(head):
        if head == None:            #handling the
            return None             #Corner Cases
        if head.next == None:
            return None
        
        curr = head
        
        while curr.next.next != None:  #Finding the 
            curr = curr.next           #Second last Node
        
        curr.next = None               #Unlink the last Node
        return head
    
# Find the middle of the Linked List 

    #Naive approach, with two traversals

    def printMiddle(head):
        if head == None:
            return 
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count = count + 1
        curr = head
        for i in range(count//2):
            curr = curr.next
        print(curr.key)

    # Efficient approach, With one traversal

    def printMiddle1(head):
        if head == None:
            return 
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print(slow.key)
        
    
# Find nth node from the end of linked list--> start from the end

## FIrst method using the length of linked list
    def printNthFromEnd(head,n):
        len = 0
        curr = head
        while curr:
            curr = curr.next
            len = len + 1
        if len < n:
            return
        curr = head
        for i in range(1, len-n+1):
            curr = curr.next
        print(curr.key)
        
    ## Second method using two pointers/References

    def printNthFromEnd2(head,n):
        if head == None:
            return
        first = head
        for i in range(n):
            if first == None:
                return
            first = first.next
        second = head
        while first != None:
            second = second.next
            first = first.next
        print(second.key)

# Remove duplicates from sorted singly linked list

    def removeDups(head):
        curr = head
        while curr != None and curr.next != None:
            if curr.key == curr.next.key:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
# Reverse a singly Linked List in Python

    # Efficient Method
    
    def reverselist1(head):
        curr = head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    # Naive Method
    
    def reverselist2(head):
        stack = []
        curr = head
        while curr is not None:
            stack.append(curr.key)
            curr = curr.next
        curr = head
        while curr is not None:
            curr.key = stack.pop()
            curr = curr.next
        return head
    
# Recursively Reverse a Linked List

    #First Method

    def reverselist3(head):
        
        if head == None:
            return head
        if head.next == None:
            return head
        
        rest_head = Node.reverselist3(head.next)
        rest_tail = head.next
        rest_tail.next = head
        head.next = None
        
        return rest_head
    
    
    
    #Second Method
    
    def reverselist4(curr, prev = None):
        if curr == None:
            return prev
        next = curr.next
        curr.next = prev
        return Node.reverselist4(next, curr)
        
    
    







#Driver Code
'''
temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30) 
temp1.next = temp2      
temp2.next = temp3
head = temp1 '''


head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(30)
#Node.printlist(head)
Node.reverselist2(head)
Node.printlist(head)


'''
head = None 
head = Node.insertBegin(head,10)
head = Node.insertBegin(head,20)
head = Node.insertBegin(head,30)
Node.printlist(head)

'''

'''
head = None
head = Node.insertEnd(head,10)
head = Node.insertEnd(head,20)
head = Node.insertEnd(head,30)
head = Node.insertEnd(head,40)
Node.printlist(head)
'''




        
