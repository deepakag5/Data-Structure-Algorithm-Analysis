# Time: O(N)
# Space: O(N)

def PostOrderRecursive(root):
    if root:
        PostOrderRecursive(root.left)
        PostOrderRecursive(root.right)
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


def postOrderTraversalDFS(root):
    if root is None:
        return []

    stack, output = [root, ], []

    while stack:
        node = stack.pop()
        output.append(node.val)

        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    return output[::-1]
