# Time O(N^2), as we are iterating over copies of both pre and post sub-arrays
# Space O(N^2), passing copies of both pre and post sub-arrays

def constructTreeRecursive(inorder, postorder):
    """
    :param inorder: list
    :param postorder: list
    :return: TreeNode
    """
    if not inorder or not postorder:
        return None

    ind = inorder.index(postorder.pop())
    root = Node(inorder[ind])
    root.right = constructTreeRecursive(inorder[ind + 1:], postorder)
    root.left = constructTreeRecursive(inorder[:ind], postorder)

    return root


# Time O(N), here the problem has been divided into two sub problems a=2(to compute left and right subtree)
# and the size of each sub-problem is half of the initial problem, b=2,  O(N^logb(a)) -- log2(2)=1, O(N)
# Space O(N), as we are passing only the indexes for both pre and post

def constructTreeRecursiveOptimized(inorder, postorder):
    """
    :param inorder: list
    :param postorder: list
    :return: TreeNode
    """
    # use unordered map to find the index in O(1) time
    inorder_map = {}
    for i, num in enumerate(inorder):
        inorder_map[num] = i

    def constructTree(start, end):
        if start > end:
            return None
        root = Node(postorder.pop())
        ind = inorder_map[root.val]
        root.right = constructTree(ind + 1, end)
        root.left = constructTree(start, ind - 1)

        return root

    return constructTree(0, len(inorder) - 1)