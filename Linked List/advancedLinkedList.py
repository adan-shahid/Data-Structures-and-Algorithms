# Here I am starting the some advanced problems of 
# Linked List.


class Node:
    def __init__(self,key):
        self.key = key
        self.next = None

## Reverse a Linked List in Groups

    # Recursive Approach, it requires O(n/k) auxillary space.

    def recRevk(head,k):
        curr = head
        prev, next = None, None
        count = 0
        while curr != None and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count = count + 1

        if next != None:
            rem_head = Node.recRevk(curr,k)
            head.next = rem_head
        return prev
    

    # Iterative approach with constant Auxillary Space.

    def iteRevk(head,k):
        curr = head
        prev_first = None
        first_pass = True
        while curr != None:
            first, prev = curr, None
            count = 0
            while curr != None and count < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count = count + 1
            if (first_pass):
                head = prev
                first_pass = False
            else:
                prev_first.next = prev
            prev_first = first
            return head
        
        








head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(30)