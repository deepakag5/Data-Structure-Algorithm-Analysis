# Time Complexity: O(N)+O(N) =O(N) , N is the total number of nodes in the given tree.
# We visit each node exactly once during dfs and then scan through visited

# Space Complexity: O(N)+O(N) = O(N), for info stored on stack and visited

def findSecondMin(root):
    if root is None:
        return None

    # this is an iterative method to perform depth first search O(N) {level order traversal}
    stack = [root]
    visited = set()

    while stack:
        node = stack.pop()
        visited.add(node.val)

        if node.left is not None:
            stack.append(node.left)

        if node.right is not None:
            stack.append(node.right)

    # print(visited)

    min_val = root.val
    second_min = float('inf')

    # cheking the visited set -  O(N)
    for val in visited:
        if min_val < val < second_min:
            second_min = val

    return second_min if second_min < float('inf') else -1


def findSecondMinOptimumSol(self, root):
    self.second_min = float('inf')
    min_val = root.val

    def traverse(node):
        if not node:
            return

        if min_val < node.val < self.second_min:
            self.second_min = node.val
        elif node.val == min_val:
            traverse(node.left)
            traverse(node.right)

    traverse(root)

    return self.second_min if self.second_min < float('inf') else -1


def findSecondMinOptimumSol_1(root):
    """
    Optimum solution without the use of instance variable

    Note : In Python 2 you cannot modify references to
    variables within functions outside of its scope.
    By wrapping the value in a list, it allows modification of
    the value without modifying the reference to the list variable.
    Hence we have
    """
    second_min = [float('inf')]
    min_val = root.val

    def traverse(node):
        if not node:
            return
        if min_val < node.val < second_min[0]:
            second_min[0] = node.val
        elif node.val == min_val:
            traverse(node.left)
            traverse(node.right)

    traverse(root)

    return second_min[0] if second_min[0] < float('inf') else -1
