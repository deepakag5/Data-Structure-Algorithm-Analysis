def sortedBSTNodes(root, nodes):
    if root is None:
        return None

    sortedBSTNodes(root.left, nodes)
    nodes.append(root)
    sortedBSTNodes(root.right, nodes)


def convertBSTtoBalanced(nodes, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    node = nodes[mid]

    node.left = convertBSTtoBalanced(nodes, start, mid - 1)
    node.right = convertBSTtoBalanced(nodes, mid + 1, end)

    return node


def normalBSTtoBalanced(root):
    if root is None:
        return None

    nodes = []
    sortedBSTNodes(root, nodes)
    n = len(nodes)

    return convertBSTtoBalanced(nodes, 0, n - 1)
