def PostOrderRecursive(root):
    if root:
        PostOrderTraversal(root.left)
        PostOrderTraversal(root.right)
        print(root.val)


def PostOrderIterative(root):
    if root is None:
        return False

    stack = []

    visited = set()

    if root is not None:
        stack.append(root)

    while len(stack) > 0:
        node = stack.pop()

        if node in visited:
            print(node.val)
        else:
            visited.add(node)
            stack.append(node)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)
