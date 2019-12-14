def mergeTwoBinaryTreesRecursive(t1, t2):
    if not t1:
        return t2

    if not t2:
        return t1

    t1.val += t2.val

    t1.left = mergeTwoBinaryTreesRecursive(t1.left, t2.left)
    t2.right = mergeTwoBinaryTreesRecursive(t1.right, t2.right)

    return t1
