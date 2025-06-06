class _Node:
#WE ARE USING 'slots' TO EFFICIENTLY ALLOCATE MEMORY

    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left, right):
        self._element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None  #THIS STORES THE REFERENCE OF THE ROOT.
    
    def maketree(self,e, left, right):
        self._root = _Node(e, left._root, right._root)

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=" ")
            self.inorder(troot._right)

    def preorder(self, troot):
        if troot:
            print(troot._element, end=" ")
            self.preorder(troot._left)
            self.preorder(troot._right)

    def postorder(self, troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end=' ')

# COUNTING THE NODES OF BINARY TREE
    def count(self, troot):
        if troot:
            x = self.count(troot._left)
            y = self.count(troot._right)
            return x + y + 1
        return 0 
    
#FINDING THE HEIGHT OF BINARY TREE.
    def height(self,troot):
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)

            if x > y:
                return x + 1
            else:
                return y + 1
        return 0

    

#NOW, WE WILL USE THIS CLASS TO CREATE BINARY TREE.
#WE ARE CREATING BINARY TREE HAVING 6 NODES.
#SO, WE WILL CREATE 6 BINARY TREE OBJECTS FOR 6 NODES.
 
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()

a = BinaryTree() #THIS IS NULL BINARY TREE.

#WE WILL START BY CREATING THE LEAF NODES.
x.maketree(40, a, a)
y.maketree(60, a, a)
z.maketree(20, x, a)
r.maketree(50, a, y)
s.maketree(30, r, a)
t.maketree(10, z, s)


print("Inorder traversal")
t.inorder(t._root) #BCZ t is THE ROOT OF TREE.
print()

print('Preorder Traversal')
t.preorder(t._root)
print()
print('Postorder Traversal')
t.postorder(t._root)
print()

print("Number of Nodes")
print(t.count(t._root))
print()
print("Height of the tree")
print(t.height(t._root)-1)



