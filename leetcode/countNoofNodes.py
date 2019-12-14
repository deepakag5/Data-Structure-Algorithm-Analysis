def countNodes(root):
    if root is None:
        return False

    stack = []

    stack.append(root)

    count = 0

    while stack:
        node = stack.pop()
        count += 1

        if node.left is not None:
            stack.append(node.left)

        if node.right is not None:
            stack.append(node.right)

    return count
