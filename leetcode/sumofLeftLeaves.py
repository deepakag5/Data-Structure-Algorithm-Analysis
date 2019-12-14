def sumofLeftLeavesBinaryTree(root):
    if root is not None:
        return False

    stack = [root]

    llsum = 0

    while stack:
        node = stack.pop()

        if node.left is not None:
            stack.append(node.left)

            if node.left.left is None and node.left.right is None:
                llsum += node.val

        if node.right is not None:
            stack.append(node.right)

    return llsum
