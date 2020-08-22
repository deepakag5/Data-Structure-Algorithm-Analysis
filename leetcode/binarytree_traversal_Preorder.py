def PreOrderRecursive(root):
    if not root:
        return None

    output = []

    def dfs(root):
        if root:
            output.append(root.val)
            dfs(root.left)
            dfs(root.right)

    dfs(root)

    return output


def PreOrderIterative(root):
    if not root:
        return False

    stack, output = [root], []

    while stack:
        node = stack.pop()
        output.append(node.val)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)
