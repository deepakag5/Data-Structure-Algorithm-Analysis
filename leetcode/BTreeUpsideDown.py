class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key



def binarytreeUpsideDown(root):
    # base case
    if root is None or root.left is None:
        return root

    newroot = Node(binarytreeUpsideDown(root.left))

    root.left.left = root.right
    root.left.right = root.right
    root.left = None
    root.right = None

    return newroot



