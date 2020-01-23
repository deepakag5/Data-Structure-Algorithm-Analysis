# O(n), O(n)

def findLCARecursive(root, n1, n2):
    """
        :param root: TreeNode
        :param n1: TreeNode
        :param n2: TreeNode
        :return: TreeNode
    """

    if root is None:
        return None

    if root.val > n1.val and root.val > n2.val:
        return findLCARecursive(root.left, n1, n2)

    elif root.val < n1.val and root.val < n2.val:
        return findLCARecursive(root.right, n1, n2)
    else:
        return root


# O(n), O(1)

def findLCAIterative(root, n1, n2):
    """
        :param root: TreeNode
        :param n1: TreeNode
        :param n2: TreeNode
        :return: TreeNode
    """
    node = root

    # base case
    if node is None:
        return None

    while node:
        # if both values are lesser than current node then by definition of BST both lie in left sub tree
        if node.val > n1.val and node.val > n2.val:
            node = node.left
        # consequently if both values are greater they lie in right sub tree
        elif node.val < n1.val and node.val < n2.val:
            node = node.right
        else:
            # we have found the split point as one value is smaller (lies in left subtree)
            # and other is higher (lies in right subtree)
            return node