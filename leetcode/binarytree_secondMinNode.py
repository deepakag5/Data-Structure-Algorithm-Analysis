def secondMinNode(root):
    unique_vals = set()

    def dfs(node):
        if node:
            unique_vals.add(node.val)
            dfs(node.left)
            dfs(node.right)

    dfs(root)

    min_val, ans = root.val, float('inf')

    for node_val in unique_vals:
        if min_val < node_val < ans:
            ans = node_val

    return ans if ans < float('inf') else -1


def secondMinNodeNoSet(self, root):
    min_val, self.ans = root.val, float('inf')

    def dfs(node):
        if node:
            if min_val < node.val < self.ans:
                self.ans = node.val
            elif min_val == node.val:
                dfs(node.left)
                dfs(node.right)

    dfs(root)

    return self.ans if self.ans < float('inf') else -1
