def bsttoGSTRecursive(root):
    def revinorder(node, val):
        if not node:
            return val
        node.val += revinorder(node.right, val)
        return revinorder(node.left, node.val)

    revinorder(root, 0)

    return root
