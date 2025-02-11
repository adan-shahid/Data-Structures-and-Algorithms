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
        
# Implement 2 stacks in a array
class twoStack:
    def __init__(self,n):
        self.size = n
        self.arr = [None]*n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1 < self.top2-1: # this ensures that array has at least space for one item
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x
            return True
        return False

    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 + 1
            self[arr.top2] = x
            return True
        return False

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1-1
            return x
        return None

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        return None
    def size1(self):
        return self.top1 + 1
    def size2(self):
        return self.size - self.top2


