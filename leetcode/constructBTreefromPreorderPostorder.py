def constructTreeRecursive(preorder, postorder):
    if not postorder:
        return None
    elif len(postorder) == 1:
        return Node(preorder.pop(0))
    else:
        root = Node(preorder.pop(0))
        pos = postorder.index(preorder[0])
        root.left = constructTreeRecursive(preorder, postorder[:pos + 1])
        root.right = constructTreeRecursive(preorder, postorder[pos + 1:-1])
        return root
