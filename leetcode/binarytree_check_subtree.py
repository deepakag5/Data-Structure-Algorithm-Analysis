# O(n^2)

def areIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return ((root1.val == root2.val) and \
            areIdentical(root1.left, root2.left) and \
            areIdentical(root1.right, root2.right))


def isSubtree(T, S):
    if S is None:
        return True

    if T is None:
        return False

    if areIdentical(T, S):
        return True

    return isSubtree(T.left, S) or isSubtree(T.right, S)
