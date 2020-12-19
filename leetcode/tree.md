+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)
+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
+ [Invert Binary Tree](#invert-binary-tree)
+ [Validate Binary Search Tree](#validate-binary-search-tree)
+ [Binary Search Tree Iterator](#)
+ [Binary Tree Level Order Traversal](#)
+ [Kth Smallest Element in a BST](#)
+ [Symmetric Tree](#)
<!-----solution----->

## Symmetric Tree



```python

def isSymmetric(self, root: TreeNode) -> bool:
    if root == None:
        return True
    def change(node):
        if node == None:
            return node
        elif node.left == None and node.right == None:
            return node
        else:
            tmp = node.right
            node.right = node.left
            node.left = tmp
            change(node.left)
            change(node.right)
    change(root.right)
    def identicalTrees(l, r):
        if l is None and r is None:
            return True
        if l is not None and r is not None:
            return ((l.val == r.val) and
            identicalTrees(l.left, r.left)and
            identicalTrees(l.right, r.right))
        return False
    return identicalTrees(root.left, root.right)
```

## Kth Smallest Element in a BST



```python

def kthSmallest(self, root: TreeNode, k: int) -> int:
    stack = []
    while root:
        stack.append(root)
        root = root.left
    root = stack.pop()
    k -= 1
    if not k:
        return root.val
    root = root.right
```

## Binary Tree Level Order Traversal



```python

def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
        return None
    cur = []
    cur.append(root)
    temp = []
    val = []
    res = []
    while cur:
        for node in cur:
            val.append(node.val)
            if node.left is not None:
                temp.append(node.left)
            if node.right is not None:
                temp.append(node.right)
        res.append(val)
        cur = temp
        val = []
        temp = []
    return res
```

## Binary Search Tree Iterator



```python

def __init__(self, root: TreeNode):
    self.nodes_sorted = []
    self.index = -1
    self._inorder(root)
def _inorder(self, root):
    if root is None:
        return
    self._inorder(root.left)
    self.nodes_sorted.append(root.val)
    self._inorder(root.right)
def next(self) -> int:
    self.index += 1
    return self.nodes_sorted[self.index]
def hasNext(self) -> bool:
    return self.index + 1 < len(self.nodes_sorted)
```

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

```python
class Solution(object):
    def isValidBST(self, node):
        order, lower = [], float('-inf')

        while order or node:
            while node:
                order.append(node)
                node = node.left
            node = order.pop()
            if node.val <= lower:
                return False
            lower = node.val
            node = node.right
    return True
```

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

```python
class Solution(object):
    def invertTree(self, root):
        return self.invert(root)

    def invert(self, node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.invert(node.left)
        self.invert(node.right)
        return node
```

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

```python
class Solution(object):
    def inorderTraversal(self, root):
        order = []
        self.traverse(root, order)
        return order

    def traverse(self, node, order):

        if node is None:
            return

        self.traverse(node.left, order)
        order.append(node.val)
        self.traverse(node.right, order)
```

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
claas TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        leftN = self.maxDepth(root.left)
        rightN = self.maxDepth(root.right)
        return max(leftN, rightN) + 1