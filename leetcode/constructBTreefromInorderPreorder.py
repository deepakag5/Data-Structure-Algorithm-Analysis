# Time O(N^2), as we are iterating over copies of both pre and post sub-arrays
# Space O(N^2), passing copies of both pre and post sub-arrays

def constructTreeRecursive(preorder, inorder):
    """
    :param preorder: list
    :param inorder: list
    :return: TreeNode
    """
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = Node(inorder[ind])
        root.left = constructTreeRecursive(preorder, inorder[0:ind])
        root.right = constructTreeRecursive(preorder, inorder[ind + 1:])

        return root


# Time O(N), here the problem has been divided into two sub problems a=2(to compute left and right subtree)
# and the size of each sub-problem is half of the initial problem, b=2,  O(N^logb(a)) -- log2(2)=1, O(N)
# Space O(N), as we are passing only the indexes for both pre and post

def constructTreeRecursiveOptimized(preorder, inorder):
    """
    :param preorder: list
    :param inorder: list
    :return: TreeNode
    """
    # we will use unordered map (dict) to save the inorder list
    # so that we can access it in O(1) time
    inorder_map = {}
    for i, num in enumerate(inorder):
        inorder_map[num] = i

    def constructTree(start, end):
        if start > end:
            return None
        root = Node(preorder.pop(0))
        ind = inorder_map[root.val]
        root.left = constructTree(start, ind - 1)
        root.right = constructTree(ind + 1, end)

        return root

    return constructTree(0, len(inorder) - 1)