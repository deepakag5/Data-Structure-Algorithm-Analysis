def findDeepestNode(root):
    if root is None:
        return False

    queue = []

    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return node.val
