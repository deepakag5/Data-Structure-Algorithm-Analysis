def InOrderRecursive(root):
    if not root:
        return []

    output = []

    def dfs(root):
        if root:
            dfs(root.left)
            output.append(root.val)
            dfs(root.right)

    dfs(root)

    return output


def InOrderIterative(root):
    if not root:
        return []

    stack, output = [], []

    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            output.append(node.val)

            node = node.right

    return output
