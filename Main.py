class BinaryTreeNode:
    """
    Binary Tree has 3 attributes
    data -> to store the data
    left_child -> to set element to left
    right_child -> to set element to right
    """
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    if (root == None):
        root = BinaryTreeNode(new_value)
        return root
    else:
        if root.data > new_value:
            if root.left_child is None:
                new_node = BinaryTreeNode(new_value)
                root.left_child = new_node
            else:
                insert(root.left_child,new_value)
                
        else:
            if root.right_child is None:
                new_node = BinaryTreeNode(new_value)
                root.right_child = new_node
            else:
                insert(root.right_child,new_value)

def inorder(root) -> None:
    """
    to print in the order
    left mid right
    """
    if root:
        inorder(root.left_child)
        print(root.data, end = " ")
        inorder(root.right_child)


def preorder(root) -> None:
    """
    to print in the order
    mid left right
    """
    if root:
        print(root.data, end = " ")
        preorder(root.left_child)
        preorder(root.right_child)


def postorder(root) -> None:
    """
    to print in the order
    left right left
    """
    if root:
        postorder(root.left_child)
        postorder(root.right_child)
        print(root.data, end = " ")

# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
