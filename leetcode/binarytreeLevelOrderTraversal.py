def LevelOrderIterative(root):
    if root is None:
        return False

    queue = []

    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)

        print(node.val)

        if node.left is None:
            queue.append(node.left)

        if node.right is None:
            queue.append(node.right)
