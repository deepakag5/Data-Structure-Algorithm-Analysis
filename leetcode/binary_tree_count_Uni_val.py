# Time: O(N)
# Space: O(h)


# within a func
def countUnivalSubtrees(root):
    count = [0]

    def dfs(root, count):
        if not root:
            return True
        left = dfs(root.left, count)
        right = dfs(root.right, count)

        if left == True and right == True:
            if root.left and root.val != root.left.val:
                return False
            if root.right and root.val != root.right.val:
                return False
            count[0] += 1
            return True

        return False

    dfs(root, count)

    return count[0]


# using a class func
class Solution:
    def countUnivalSubtrees(self, root):
        self.count = 0
        self.dfs(root)
        return self.count

    def dfs(self, root):
        if not root:
            return True

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left == True and right == True:
            if root.left and root.val != root.left.val:
                return False
            if root.right and root.val != root.right.val:
                return False
            self.count += 1
            return True

        return False
