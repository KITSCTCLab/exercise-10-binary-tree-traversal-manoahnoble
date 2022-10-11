class BinaryTreeNode:
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
    # Write your code here
    if root==None:
        root=BinaryTreeNode(new)
        return root
    else:
        if root.data > new:
            if root.left_child is None:
                node = BinaryTreeNode(new)
                root.left_child = node
            else:
                insert(root.left_child,new)
        else:
            if root.right_child is None:
                node = BinaryTreeNode(new)
                root.right_child = node
            else:
                insert(root.right_child,new)


def inorder(root) -> None:
    # Write your code here


def preorder(root) -> None:
    # Write your code here


def postorder(root) -> None:
    # Write your code here


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
