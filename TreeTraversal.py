Skip to content
Logo
Home
Python Course
Start Here
Preorder Tree Traversal in Python
Preorder Tree Traversal In Python

In this article, we will study the concept and algorithm for preorder tree traversal. Then we will implement the algorithm for preorder traversal in Python and run it on a binary tree.

What is Preorder Tree Traversal?
Preorder traversal is a depth-first tree traversal algorithm. In depth-first traversal, we start at the root node and then we explore a branch of the tree till the end and then we backtrack and traverse another branch.

In the preorder traversal, first, we traverse the current node, and then we traverse the left child or left subtree of the current node, and then we traverse the right child or right subtree of the current node. We perform this operation recursively till all the nodes are traversed.


We use preorder traversal to create a copy of a binary tree. We can also derive the prefix expression from an expression tree using preorder traversal. 

Preorder Tree Traversal Algorithm in Python
Following is the algorithm of preorder tree traversal.


Algorithm preorder –

Input: Reference to Root Node
Output: Prints All the nodes of the tree
Start.
If the root is empty, return.
Traverse the root node. //print value at node
Traverse left subtree of the root.// preorder(root.leftChild)
Traverse the right subtree of the root.// preorder(root.rightChild)
End.
Preorder Traversal Algorithm Implementation in Python
Now we will implement the above algorithm to print nodes of the following binary tree in preorder traversal.

Askpython31 1
Binary Tree
In the following code, first the above binary tree has been created and then preorder traversal of the binary tree is printed.

class BinaryTreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild=None
     
def insert(root,newValue):
    #if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root=BinaryTreeNode(newValue)
        return root
    #binary search tree is not empty, so we will insert it into the tree
    #if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue<root.data:
        root.leftChild=insert(root.leftChild,newValue)
    else:
        #if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild=insert(root.rightChild,newValue)
    return root
def preorder(root):
    #if root is None return
        if root==None:
            return
        #traverse root
        print(root.data)
        #traverse left subtree
        preorder(root.leftChild)
        #traverse right subtree
        preorder(root.rightChild)                   
root= insert(None,15)
insert(root,10)
insert(root,25)
insert(root,6)
insert(root,14)
insert(root,20)
insert(root,60)
print("Printing values of binary tree in preorder Traversal.")
preorder(root)
