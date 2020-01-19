# Time: O(n)
# Space: O(n) - to keep tree

def validateRecursive(root):
    if not root:
        return True

    def recurse(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
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
        return True

    stack = [(root, float('-inf'), float('inf')), ]

    while stack:
        node, lower, upper = stack.pop()
        if not node:
            continue
        val = node.val
        print(val)
        print("lower: " + str(lower))
        print("upper: " + str(upper))

        if val <= lower or val >= upper:
            return False
        # we are appending right and then left node in stack so when loop
        # gets called again last value appended which is left will get popped (LIFO)
        # also for right node you want to compare with its left value hence change lower to val
        # for left node you want compare with right node value hence change upper to val
        stack.append((node.right, val, upper))
        stack.append((node.left, lower, val))

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


class Node:

    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


root = Node(2)
root.left = Node(1)
root.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(6)

print(validateIterative(root))
