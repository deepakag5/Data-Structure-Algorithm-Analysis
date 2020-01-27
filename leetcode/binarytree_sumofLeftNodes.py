def sumofleftnodesBinaryTree(root):
    if root is None:
        return False

    # or we can directly write stack = [root]
    stack = []
    stack.append(root)

    lsum = 0

    while stack:
        node = stack.pop()

        if node.left is not None:
            stack.append(node.left)
            lsum += node.val

        if node.right is not None:
            stack.append(node.right)

    return lsum
