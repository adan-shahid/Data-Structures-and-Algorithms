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


#NOW, WE WILL USE THIS CLASS TO CREATE BINARY TREE.
#WE ARE CREATING BINARY TREE HAVING 3 NODES.
#SO, WE WILL CREATE 3 BINARY TREE OBJECTS FOR 3 NODES.
 
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()

a = BinaryTree()
x.maketree(20, a, a)
y.maketree(30, a, a)
z.maketree(10,x,y)


print("Inorder traversal")
z.inorder(z._root)
print()

print('Preorder Traversal')
z.preorder(z._root)
print()
print('Postorder Traversal')
z.postorder(z._root)



