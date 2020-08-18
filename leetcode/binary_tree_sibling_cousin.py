class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.right.right.left = Node(10)
root.right.right.right = Node(11)


# function to get sibling value
def get_sibling(root, node):
    if not root or root.val == node.val:
        return None

    if root.left and root.left.val == node.val:
        return root.right

    if root.right and root.right.val == node.val:
        return root.left

    sib = get_sibling(root.left, node)

    if sib is not None:
        return sib

    sib = get_sibling(root.right, node)

    return sib


# helper functions to get cousin
# get level of a node in binary tree
def get_level(root, node, level):
    if not root:
        return 0

    if root.val == node.val:
        return level

    left_level = get_level(root.left, node, level + 1)

    if left_level != 0:
        return left_level

    return get_level(root.right, node, level + 1)


def print_cousins(root, node, level):
    if not root or level < 2:
        return

    if level == 2:
        if (root.left and root.left.val == node.val) or (root.right and root.right.val == node.val):
            return

        if root.left:
            print("cousin: " + str(root.left.val))

        if root.right:
            print("cousin: " + str(root.right.val))

    elif level > 2:
        print_cousins(root.left, node, level - 1)
        print_cousins(root.right, node, level - 1)


def get_both_sibling_and_cousin(root, node):
    sibling = get_sibling(root, node)

    level = get_level(root, node, 1)

    if sibling:
        print("sibling: " + str(sibling.val))

    print_cousins(root, node, level)


get_both_sibling_and_cousin(root, root.left.left)


# We can get both sibling and cousing in a single pass
def print_sibling_and_cousin(root, node, level):
    if not root or level < 2:
        return

    if level == 2:
        if root.left and root.left.val == node.val:
            if root.right:
                print("Sibling: " + str(root.right.val))
            return

        if root.right and root.right.val == node.val:
            if root.left:
                print("Sibling: " + str(root.left.val))
            return

        if root.left:
            print("Cousin: " + str(root.left.val))

        if root.right:
            print("Cousin: " + str(root.right.val))

    elif level > 2:
        print_sibling_and_cousin(root.left, node, level - 1)
        print_sibling_and_cousin(root.right, node, level - 1)


def get_sibling_cousing_single_pass(root, node):
    level = get_level(root, node, 1)

    print_sibling_and_cousin(root, node, level)


get_sibling_cousing_single_pass(root, root.left.left)

# Time: O(n) we may need to visit all nodes in worst case
# Space: O(1) we don't use any extra space (but if we consider recursion stack then space is O(n))
