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

# Implement K stacks in an array
class kStacks:
    def __init__(self,n,k):
        self.cap = n
        self.k = k
        self.arr = [None]*n
        self.top = [-1]*k
        self.next = [i+1 for i in range(n)]
        self.next[n-1] = -1
        self.free_top = 0

    def push(self, sn, x):
        i = self.free_top
        self.free_top = self.next[self.free_top]
        self.arr[i] = x
        self.next[i] = self.top[sn]
        self.top[sn] = i

    def pop(self, sn):
        prev.top = self.top[sn]
        self.top[sn] = next[prev_top]
        self.next[prev_top] = self.free_top
        self.free_top = prev.top
        return self.arr[prev_top]

    def isEmpty(self,sn):
        return self.top[sn] == -1

# stock Span Problem--> given array represents the pieces of stock i=on 'n' consective days
    #span on a day------ No is of consective days(icnluding the current one) and days before it, which has value
    # equal or smaller

    # Naive Solution
def printSpan(arr):
    for i in range(len(arr)):
        span = 1
        j = i - 1
        while j >= 0 and arr[i] >= arr[j]:
            span += 1
            j -= 1
        print(span, end="")

    # Efficient Solution-----Linear Time
def printSpan1(arr):
    st = []
    st.append(0)
    print(1, end="")
    for i in range(1,n):
        while (len(st) >= 0 and arr[st[-1]] <= arr[i]):
            st.pop()
        span = (i+1) if len(st) == 0 else i-st[-1]
        print(span, end="")
        st.append(i)

# Previous Greater Element
    # Naive Solutoion
def prevGreater(arr):
    for i in range(len(arr)):
        pg = -1
        for j in range(i-1, -1, -1):
            if arr[j] > arr[i]:
                pg = arr[j]
                break
        print(pg, end="")


    # Efficient Solution
def prevGreater1(arr):
    st = []
    for i in range(len(arr)):
        while len(st) > 0 and st[-1] <= arr[i]:
            st.pop()
        pg = -1 if (len(st)==0) else st[-1]
        print(pg, end = "")
        st.append(arr[i])

# Next greater element
    # Naive Solution
def printNextGreater(arr):
    for i in range(len(arr)):
        ng = -1
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                ng = arr[j]
                break
            print(ng, end = "")

    # Efficient Solution

def nextGreater(arr):
    st = []
    res=[None]*len(arr)
    for i in range(n-1, -1, -1):
        while len(st) > 0 and st[-1] <= arr[i]:
            st.pop()
        res[i] = -1 if len(st) == 0 else st[-1]
        st.append(arr[i])
    for x in res:
        print(x, end="")

# Largest Rectangular Area in a Histogram
    # Naive Solution--> O(n**2)
def getMaxArea(arr):
    res = 0
    n = len(arr)
    for i in range(n):
        curr = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] >= arr[i]:
                curr += arr[i]
            else:
                break
        for j in range(i+1, n):
            if arr[j] >= arr[i]:
                curr += arr[i]
            else:
                break
        res = max(res, curr)
    return res

    # Efficient Solution
def getMaxArea1(arr):
    st = []
    res = 0
    for i in range(len(arr)):
        while st and arr(st[-1]) >= arr[i]:
            tp = st[-1]
            st.pop()
            curr_width = (i-st[-1]-1) if st else i
            res = max(res, curr_width*arr[tp])
        st.append(i)
    while st:
        tp= st[-1]
        st.pop()
        curr_width - (len(arr)-st[-1]-1) if st else len(arr)
        res = max(res, curr_width*arr[tp])
    return res

# Largest Rectangle with all 1's
    # We are given a boolean matrix, and we need to find out 
    # largest submatrix with all 1's

def maxRectangle(mat):
    res = getMaxArea1(mat[0])
    for i in range(1, len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]:
                mat[i][j] += mat[i-1][j]
        res= max(res, getMaxArea1(mat[i]))
    return res

            
