def find(root, v):
    """
    find the value in tree
    :param root: TreeNode
    :param v: val[int]
    :return: boolean

    """

    if root is None:
        return None

    if root.val == v or find(root.left, v) or find(root.right, v):
        return True

    return False


def findLCA(root, n1, n2, v):
    """
    finds the lca
    :param root: TreeNode
    :param n1: val[int]
    :param n2: val[int]
    :return: TreeNode

    """
    if root is None:
        return True

    if root.val == n1:
        v[0] = True
        return root

    if root.val == n2:
        v[1] = True
        return root

    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    # one key is present in left sub-tree and other in right sub-tree then lca is root
    if left_lca and right_lca:
        return root

    if left_lca is not None:
        return left_lca
    else:
        return right_lca


def findLCAinBTree(root, n1, n2):
    """
    find and returns the lca if both values are present otherwise returns None
    :param root:TreeNode
    :param n1: val[int]
    :param n2: val[int]
    :return: TreeNode

    """
    v = [False, False]

    lca = findLCA(root, n1, n2, v)

    # returns lca if both n1 and n2 are present in the tree
    if (v[0] and v[1]) or (v[0] and find(lca, n2)) or (v[1] and find(lca, n1)):
        return lca

    return None
