def LevelOrderIterative(root):
    if root is None:
        return False

    queue = []

    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)

        print(node.val)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


def levelOrderRecursive(root):
    levels = []

    if not root:
        return levels

    def getlevelorder(node, level):
        # starting the current level
        if len(levels)==level:
            levels.append([])

        levels[level].append(node.val)

        if node.left is not None:
            getlevelorder(node.left, level+1)

        if node.right is not None:
            getlevelorder(node.right, level+1)

    getlevelorder(root, 0)

    return levels