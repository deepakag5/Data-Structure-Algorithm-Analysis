def levelOrderRecursive(root):
    """
    :param root: TreeNode
    :return: List
    """
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



def levelorderIterative(root):
    """
    :param root: TreeNode
    :return: List
    """
    if not root:
        return []

    queue = []
    levels = []

    level = 0

    queue.append(root)

    while queue:
        levels.append([])
        level_length = len(queue)

        for i in range(level_length):
            node = queue.pop(0)
            levels[level].append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level+=1

    return levels