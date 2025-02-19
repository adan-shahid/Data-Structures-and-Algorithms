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
    n = len(arr)
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

# Infix to postfix conversion using stack

# Python program to convert infix expression to postfix
# Class to convert the expression


class Conversion:

	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		self.array = []
		self.output = []
		self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

	def isEmpty(self):
		return True if self.top == -1 else False

	def peek(self):
		return self.array[-1]

	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"

	def push(self, op):
		self.top += 1
		self.array.append(op)

	def isOperand(self, ch):
		return ch.isalpha()

	def notGreater(self, i):
		try:
			a = self.precedence[i]
			b = self.precedence[self.peek()]
			return True if a <= b else False
		except KeyError:
			return False

	def infixToPostfix(self, exp):

		for i in exp:
			if self.isOperand(i):
				self.output.append(i)

			elif i == '(':
				self.push(i)

			elif i == ')':
				while((not self.isEmpty()) and
					self.peek() != '('):
					a = self.pop()
					self.output.append(a)
				if (not self.isEmpty() and self.peek() != '('):
					return -1
				else:
					self.pop()

			else:
				while(not self.isEmpty() and self.notGreater(i)):
					self.output.append(self.pop())
				self.push(i)

		while not self.isEmpty():
			self.output.append(self.pop())

		print ("".join(self.output))


# Driver's code
if __name__ == '__main__':
	exp = "a+b*(c^d-e)^(f+g*h)-i"
	obj = Conversion(len(exp))

	# Function call
	obj.infixToPostfix(exp)

# Python program to evaluate value of a postfix expression
class Evaluate:	
	def __init__(self, capacity):
		self.top = -1
		self.capacity = capacity
		self.array = []
	
	def isEmpty(self):
		return True if self.top == -1 else False
	
	def peek(self):
		return self.array[-1]
	
	def pop(self):
		if not self.isEmpty():
			self.top -= 1
			return self.array.pop()
		else:
			return "$"
	
	def push(self, op):
		self.top += 1
		self.array.append(op)

	def evaluatePostfix(self, exp):
		
		for i in exp:
			
			if i.isdigit():
				self.push(i)

			else:
				val1 = self.pop()
				val2 = self.pop()
				self.push(str(eval(val2 + i + val1)))

		return int(self.pop())
				

			
# Driver program to test above function
exp = "231*+9-"
obj = Evaluate(len(exp))
print ("postfix evaluation: %d"%(obj.evaluatePostfix(exp)))

# Python program to convert infix to prefix.

def isOperator(c):
	return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))

def getPriority(C):
	if (C == '-' or C == '+'):
		return 1
	elif (C == '*' or C == '/'):
		return 2
	elif (C == '^'):
		return 3
	return 0

def infixToPrefix(infix):
	operators = []

	operands = []

	for i in range(len(infix)):
		if (infix[i] == '('):
			operators.append(infix[i])

		elif (infix[i] == ')'):
			while (len(operators)!=0 and operators[-1] != '('):
				op1 = operands[-1]
				operands.pop()

				op2 = operands[-1]
				operands.pop()

				op = operators[-1]
				operators.pop()

				tmp = op + op2 + op1
				operands.append(tmp)

			operators.pop()

		elif (not isOperator(infix[i])):
			operands.append(infix[i] + "")

		else:
			while (len(operators)!=0 and getPriority(infix[i]) <= getPriority(operators[-1])):
				op1 = operands[-1]
				operands.pop()

				op2 = operands[-1]
				operands.pop()

				op = operators[-1]
				operators.pop()

				tmp = op + op2 + op1
				operands.append(tmp)
			operators.append(infix[i])

	while (len(operators)!=0):
		op1 = operands[-1]
		operands.pop()

		op2 = operands[-1]
		operands.pop()

		op = operators[-1]
		operators.pop()

		tmp = op + op2 + op1
		operands.append(tmp)

	return operands[-1]

s = "(A-B/C)*(A/K-L)"
print( infixToPrefix(s))

#Python program to evaluate a prefix expression.

def is_operand(c):
	return c.isdigit()


def evaluate(expression):
	stack = []

	for c in expression[::-1]:

		if is_operand(c):
			stack.append(int(c))

		else:
			o1 = stack.pop()
			o2 = stack.pop()

			if c == '+':
				stack.append(o1 + o2)

			elif c == '-':
				stack.append(o1 - o2)

			elif c == '*':
				stack.append(o1 * o2)

			elif c == '/':
				stack.append(o1 / o2)

	return stack.pop()


# Driver code
if __name__ == "__main__":
	test_expression = "+9*26"
	print(evaluate(test_expression))






            
