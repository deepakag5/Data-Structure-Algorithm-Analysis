def findLCARecursive(root, n1, n2):
    if root is None:
        return None

    if root.val > n1 and root.val > n2:
        return findLCARecursive(root.left, n1, n2)

    if root.val < n1 and root.val < n2:
        return findLCARecursive(root.right, n1, n2)

    return root
