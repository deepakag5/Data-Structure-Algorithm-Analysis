# Time: O(n)
# Space: O(n) - to keep tree

def validateRecursive(root):
    if not root:
        return None

    def recurse(node, lower=float('-inf'), upper=float('inf')):
        val = node.val
        if val <= lower or val >= upper:
            return False

        if not recurse(node.right, val, upper):
            return False
        if not recurse(node.left, lower, val):
            return False

        return True

    return recurse(root)


# Time: O(n)
# Space: O(n) - to keep tree

def validateIterative(root):
    if not root:
        return False

    stack = [(root, float('-inf'), float('inf')), ]

    while stack:
        root, lower, upper = stack.pop()

        val = root.val

        if val <= lower and val >= upper:
            return False
        stack.append((root.right, val, upper))
        stack.append(root.left, lower, val)

    return True


# Time: O(n)
# Space: O(n) - for stack

def validateInorder(root):
    stack, inorder = [], float('-inf')

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if root.val <= inorder:
            return False

        inorder = root.val
        root = root.right

    return True
