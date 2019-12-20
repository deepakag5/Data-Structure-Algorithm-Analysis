def deletedeepestNode(root, deep_node):
    queue = []
    queue.append(root)

    while len(q):
        temp = queue.pop(0)
        if temp is deep_node:
            temp = None
            return
        if temp.right:
            if temp.right is deep_node:
                temp.right = None
                return
            else:
                queue.append(temp.right)

        if temp.left:
            if temp.left is deep_node:
                temp.left = None
                return
            else:
                queue.append(temp.left)
