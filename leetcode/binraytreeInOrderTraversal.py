def InOrderRecursive(root):
    if root:
        InOrderRecursive(root.left)

        print(root.val)

        InOrderRecursive(root.right)


def InOrderIterative(root):
    if not root:
        return False

    stack = []

    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.val)

            node = node.right
