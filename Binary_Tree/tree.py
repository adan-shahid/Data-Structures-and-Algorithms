class _Node:
#WE ARE USING 'slots' TO EFFICIENTLY ALLOCATE MEMORY

    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left, right):
        self._element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None
    
    def maketree(self,e, left, right):
        self._root = _Node(e, left._root, right._root)
