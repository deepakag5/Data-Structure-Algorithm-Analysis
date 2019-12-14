def mergeTwoBinaryTreesRecursive(t1, t2):
    if not t1:
        return t2

    if not t2:
        return t1

    t1.val += t2.val

    t1.left = mergeTwoBinaryTreesRecursive(t1.left, t2.left)
    t2.right = mergeTwoBinaryTreesRecursive(t1.right, t2.right)

    return t1


def mergeTwoBinaryTreesIterative(t1, t2):
    if not t1:
        return t2

    if not t2:
        return t1

    stack = []

    stack.append(t1)
    stack.append(t2)

    while stack:
        node2 = stack.pop()
        node1 = stack.pop()

        node1.val += node2.val

        if node1.left is not None:
            stack.append(node1.left)
            stack.append(node2.left)
        if node1.left is None:
            node1.left = node2.left

        if node1.right is not None:
            stack.append(node1.right)
            stack.append(node2.right)
        if node1.right is None:
            node1.right = node2.right

    return t1
