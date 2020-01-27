def PreOrderRecursive(root):
    if root:
        print(root.val)

        printPreOrder(root.left)

        printPreOrder(root.right)


def PreOrderIterative(root):
    if not root:
        return False

    stack = []

    stack.append(root)

    while stack:
        node = stack.pop()
        print(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)
