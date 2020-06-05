# Time: O(N) - we visit each node exactly once
# Space: O(N) worst case - O(log N) when tree is completely balanced


def findPathSumExistsRecursive(root, target_sum):
    """

    :param root: TreeNode
    :param target_sum: path sum value [int]
    :return: boolean

    """
    if not root:
        return None

    target_sum -= root.val

    # when we reach a leaf node check whether the remaining target_sum
    # has become zero which means we have find our desired path
    if root.left is None and root.right is None:
        return target_sum == 0

    return findPathSumExistsIterative(root.left, target_sum) \
           or findPathSumExistsIterative(root.right, target_sum)


# Time: O(N) - we visit each node exactly once
# Space: O(N) worst case - O(log N) when tree is completely balanced

def findPathSumExistsRecursive_1(root, target_sum):
    """

    :param root: TreeNode
    :param target_sum: path sum value [int]
    :return: boolean

    """
    exist = []

    def findPathSum(root, target, exist):
        if root:
            if root.left is None and root.right is None:
                if root.val == target:
                    exist.append(True)

            if root.right is not None:
                findPathSum(root.right, target - root.val, exist)

            if root.left is not None:
                findPathSum(root.left, target - root.val, exist)

    findPathSum(root, target_sum, exist)

    return any(exist)


# Time: O(N) - we visit each node exactly once
# Space: O(N) worst case - O(log N) when tree is completely balanced

def findPathSumExistsIterative(root, target_sum):
    """

    :rtype: object
    :param root: TreeNode
    :param target_sum: path sum value [int]
    :return: boolean

    """

    if root is None:
        return False

    stack = [(root, target_sum - root.val), ]

    while stack:
        node, curr_sum = stack.pop()

        # when we reach a leaf node check whether the remaining target_sum
        # has become zero which means we have find our desired path
        if node.left is None and node.right is None and curr_sum == 0:
            return True

        if node.right:
            stack.append((node.right, curr_sum - node.right.val))

        if node.left:
            stack.append((node.left, curr_sum - node.left.val))

    return False
