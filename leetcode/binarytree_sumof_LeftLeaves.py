# Time: O(N)
# Space: O(N)


def sumOfLeftLeavesRecursive(root):
    left_leaves_sum = [0]

    def dfs(root):
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        left_val = dfs(root.left)
        left_leaves_sum[0] += left_val

        dfs(root.right)

        return 0

    dfs(root)
    return left_leaves_sum[0]


def sumOfLeftLeavesRecursive_1(root):
    left_leaves_sum = [0]

    def dfs(root):
        if not root:
            return

        if root.left and not root.left.left and not root.left.right:
            left_leaves_sum[0] += root.left.val

        dfs(root.left)
        dfs(root.right)

    dfs(root)

    return left_leaves_sum[0]


def sumOfLeftLeavesIterative(root):
    if not root:
        return 0

    left_leaves_sum = 0

    stack = [root]

    while stack:
        node = stack.pop()

        if node.left:
            stack.append(node.left)
            if not node.left.left and not node.left.right:
                left_leaves_sum += node.left.val

        if node.right:
            stack.append(node.right)

    return left_leaves_sum
