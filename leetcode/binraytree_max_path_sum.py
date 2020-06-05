# Time: O(N)
# Space: O(log N) to keep recursion stack


def maxPathSum(root):
    def max_gain(node):
        nonlocal max_sum
        if not root:
            return 0

        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        price_newpath = node.val + left_gain + right_gain

        # take max of either max sum or price new path as
        # root need not necessarily be in max sum
        # it can be any sub-tree
        max_sum = max(max_sum, price_newpath)

        return node.val + max(left_gain, right_gain)

    max_sum = float('-inf')
    max_gain(root)

    return max_sum
