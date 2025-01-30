# Linked List implementation of Stack
import math
class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

class myStack:
    def __init__(self):

        self.head = None
        self.sz = 0

    def push(self,x):
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.sz = self.sz + 1
    
    def size(self):
        return self.sz

    def peek(self):
        if self.head == None:
            return math.inf
        return self.head.data
    
    def pop(self):
        if self.head == None:
            return math.inf
        res = head.data
        self.head = self.head.next
        self.sz = self.sz - 1
        return res
    
# Driver Code

s = myStack()
s.push(10)
s.push(20)
s.push(30)

# Check for Balanced paranthesis:

def isBalanced(expr):
    stack = []
    for x in expr:
        if x in ('(', '{','['):
            stack.append(x)
        else:
            if not stack:
                return False
            else:
                if isMatching(stack[-1],x) == False:
                    return False
                else:
                    stack.pop()
    if stack:
        return False
    else:
        return True
def isMatching(a,b):
    if (a=='(' and b == ')')or\
        (a=='[' and b == ']')or\
        (a=='{' and b == '}'):
        return True
    else:
        return False
        

