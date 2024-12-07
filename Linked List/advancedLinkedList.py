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
        

# Detect a loop in a Linked List using Floyd's Cycle Algorithm

    def isLoop(head):
        slow_p = head
        fast_p = head
        while fast_p != None and fast_p.next != None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False
    

# Detect and Remove a Loop in a Linked List.

    def detectRemoveloop(head):
        slow = head
        fast = head
        while fast != None and fast.next != None:  # Detecting the Loop
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return 
        slow = head
        while slow.next != fast.next:  # Removing the loop
            slow = slow.next
            fast = fast.next
        fast.next = None
    


        









head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(30)