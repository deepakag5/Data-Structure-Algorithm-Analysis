def searchRecursive(root, node):
    """

   :param root: TreeNode
   :param node: TreeNode
   :return: TreeNode

   """
    if root is None or root.val == node.val:
        return root

    if root.val < node.val:
        searchRecursive(root.right, node)

    return searchRecursive(root.left, node)
