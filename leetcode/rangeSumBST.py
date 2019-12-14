def rangeSUM(root, L, R):
    if root is None:
        return False

    stack = [root]

    ans = 0

    while stack:
        node = stack.pop()

        if L <= node.val <= R:
            ans += node.val

        if L < node.val:
            stack.append(node.left)

        if node.val < R:
            stack.append(node.right)

    return ans
