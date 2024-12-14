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


# Intersection point of two Linked Lists

    def getIntersection1(head1,head2): #  it will take O(m) Auxillary Space, m-->head1 
        s = set
        curr = head1
        while curr != None:
            s.add(curr)
            curr = curr.next
        curr = head2
        while curr != None:
            if curr in s:
                return curr.key
            curr = curr.next
        return -1


    # With O(1) or contt. Auxillary Space

    def getIntersection2(d, head1, head2):
        curr1 = head1
        curr2 = head2
        for i in range(d):
            if curr1 == None:
                return -1
            curr1 = curr1.next
        while curr1 != None and curr2 != None:
            if curr1 == curr2:
                return curr1.key
            curr1 = curr1.next
            curr2 = curr2.next

# Segregate Even & Odd Node in Linked List

    def segregate(head):
        es, ee, os, oe = None, None, None, None
        curr = head
        while curr != None:
            x = curr.key
            if x % 2 == 0:
                if es == None:
                    es = curr
                    ee = es
                else:
                    ee.next = curr
                    ee = ee.next
            else:
                if os == None:
                    os = curr
                    oe = os
                else:
                    oe.next = curr
                    oe = oe.next
            curr = curr.next
        if os == None or es == None:
            return head
        ee.next = os
        os.next = None
        return es

# Pairwise Swap Nodes.

    # Naive Method--> Swapping Data.

    def pairwiseSwap1(head):
        curr = head
        while curr != None and curr.next != None:
            curr.key, curr.next.key = curr.next.key, curr.key
            curr = curr.next.next
        return head


    # Efficient Approach--> By changing the Links

    def pairwiseSwap2(head):
        if head == None or head.next == None:
            return head
        curr = head.next.next
        prev = head
        head = head.next
        head.next = prev
        while curr != None and curr.next != None:
            prev.next = curr.next
            prev = curr
            next = curr.next.next
            curr.next.next = curr
            curr = next
        prev.next = curr
        return head

# Clone a Linked List with Random connections.



        


        









head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(30)