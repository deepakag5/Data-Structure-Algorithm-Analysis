def inorderSuccesor(root, node):
    if node.right is not None:
        return minValue(node.right)

    while root is not None:
        if node.val < root.val:
            succ = root
            root = root.left
        elif node.val > root.val:
            root = root.right
        else:
            break

    return succ


def minValue(node):
    current = node

    while current is not None:
        if current.left is None:
            break
        current = current.left

    return current
