# Time Complexity : O(n)

def countModeBSTree(root):
    """

    :param root: TreeNode
    :return: list[0]
    """
    cnt = {}

    def countMode(root):
        if root is None:
            return None
        else:
            cnt[root.val] = cnt.get(root.val, 0) + 1
            countMode(root.left)
            countMode(root.right)

    countMode(root)

    max_cnt = max(cnt.values())

    # if there is mode then return it (freq greater than 1) or return root node value
    if max_cnt > 1:
        return [k for k, v in cnt.items() if v == max_cnt]

    return [list(cnt.keys())[0]]
