#Deque in python
from collections import deque
# here deque uses the doubly linked list 

d = deque() # []
d.append(10)
d.append(20)
d.append(30)
d.appendleft(40)
d.insert(2,10) # item 10 at index 2
d.extend([50, 60])
d.extendleft([15, 25])
print(d)
print(d.count(10))
print(d[0])
print(d[-1]) 

# Linked list implementation of Deque
class Node:
    def __init__(self, k):
        self.key = k
        self.next = None
        self.prev = None


class MyDeque:
    def __init__(self, c):
        self.front = None
        self.rear = None
        self.sz = 0

    def size(self):
        return self.sz

    def isEmpty(self):
        return self.sz == 0

    def insertRear(self, x):
        temp = Node(x)
        if self.rear == None:
            self.front = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear
        self.rear = temp
        self.sz = self.sz + 1

    def deletfront(self):
        if self.front == None:
            return None
        else:
            res = self.front.key
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            self.sz = self.sz - 1

            return res

    def getFront(self):
        if self.front:
            return self.front.key

    def getRear(self):
        if self.rear:
            return self.rear.key

# driver code

dq = MyDeque(3)

print(dq.isEmpty())
dq.insertRear(10)
print(dq.getFront(),dq.getRear())
dq.insertRear(20)
print(dq.getFront(),dq.getRear())
dq.insertRear(30)
print(dq.getFront(), dq.getRear())
dq.deletfront()
print(dq.getFront(), dq.getRear())

print('list implementation\n')


# List implementaion of Deque
class MyDeque:
    def __init__(self, c):
        self.l = [None] * c
        self.cap = c
        self.size = 0
        self.front = 0

    def deleteFront(self):
        if self.size == 0:
            return None
        else:
            res = self.l[self.front]
            self.front = (self.front + 1) % self.cap
            self.size = self.size - 1

            return res

    def insertFront(self, x):

        if self.size == self.cap:
            return
        else:
            self.front = (self.front - 1) % self.cap
            self.l[self.front] = x
            self.size = self.size + 1

    def insertRear(self, x):
        if self.size == self.cap:
            return
        new_rear = (self.front + self.size) % self.cap
        self.l[new_rear] = x
        self.size = self.size + 1

    def deleteRear(self):
        sz = self.size
        if sz == 0:
            return None
        else:
            rear = (self.front + sz - 1) % self.cap
            self.size = sz - 1
            return self.l[rear]

    def frontEle(self):
        return self.l[self.front]

    def rearEle(self):
        rear = (self.front + self.size - 1) % self.cap
        return self.l[rear]

#Driver code
dq = MyDeque(4)

dq.insertRear(10)
print(dq.frontEle(), dq.rearEle())
dq.insertFront(20)
print(dq.frontEle(), dq.rearEle())
dq.insertFront(30)
print(dq.frontEle(), dq.rearEle())
dq.deleteRear()
print(dq.frontEle(), dq.rearEle())
dq.insertRear(40)
print(dq.frontEle(), dq.rearEle())
dq.deleteRear()
print(dq.frontEle(), dq.rearEle())
