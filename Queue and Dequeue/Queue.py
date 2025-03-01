# Linked list implementation of Queue in python

class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    def size(self):
        return self.size
    def isEmpty(self):
        return(self.sz == 0)
    def getFront(self):
        return self.front.key
    def getRear(self):
        return self.rear.key
    def enque(self,x):
        temp = Node(x)
        if self.rear == None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.sz = self.sz + 1
    def deque(self):
        if self.front == None:
            return None
        else:
            res = self.front.key
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self.sz = self.sz - 1
            return res
        # End of class MyQueue 

# Queue implementation using circular list
class Myqueue:
    def __init__(self,c):
        self.l = [None]*c
        self.cap = c
        self.size = 0
        self.front = 0
    def getFront(self):
        if self.size == 0:
            return None
        else:
            return self.l[self.front]
    def getRear(self):
        if self.size == 0:
            return None
        else:
            rear = (self.front + self.size-1) % self.cap
            return self.l[rear]
    def enque(self,x):
        if self.size == self.cap:
            return 
        else:
            rear = (self.front+self.size-1) % self.cap
            rear = (rear+1) % self.cap
            self.l[rear] = x
            self.size = self.size + 1
    def deque(self):
        if self.size == 0:
            return None
        else:
            res = self.l[self.front]
            self.front = (self.front+1)%self.cap
            self.size = self.size - 1
            return res


        

        