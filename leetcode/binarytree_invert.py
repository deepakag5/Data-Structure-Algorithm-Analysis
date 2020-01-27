def invertBTreeRecursive(root):
    if root is None:
        return False
    else:
        node = root

        invertBTreeRecursive(root.left)
        invertBTreeRecursive(root.right)

        node = root.left
        root.left = root.right
        root.right = node

    return root


def inverBTreeIterative(root):
    if root is None:
        return False

    stack = [root]

    while stack:
        node = stack.pop()

        node.left, node.right = node.right, node.left

        if node.left is not None:
            stack.append(node.left)

        if node.right is not None:
            stack.append(node.right)

    return root
