class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key



def binarytreeUpsideDownRecursive(root):
    """
    :param root: TreeNode
    :return: TreeNode
    """
    # base case
    if root is None or root.left is None:
        return root

    # assign new root as left most child
    newroot = binarytreeUpsideDownRecursive(root.left)

    root.left.left = root.right
    root.left.right = root
    root.left = None
    root.right = None

    return newroot



def binarytreeUpsideIterative(root):
    curr = root
    temp = None
    prev = None

    while curr is not None:
        next = curr.left

        # swap nodes
        curr.left = temp
        temp = curr.right
        curr.right = prev

        prev = curr
        curr = next

    return prev
