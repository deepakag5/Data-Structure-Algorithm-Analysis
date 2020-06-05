# this is the simplest implementation which assumes that both the
# values are present in the tree, if one of the values is not present
# it will return the node which is present in the tree
# if both the values are not present then it will return None

# O(n), O(n)

def lowestCommonAncestorRecursive(root, p, q):
    """
    :param root: TreeNode
    :param p: TreeNode
    :param q: TreeNode
    :return: TreeNode
    """
    if root is None:
        return None

    if root.val == p.val or root.val == q.val:
        return root

    left = lowestCommonAncestorRecursive(root.left, p, q)
    right = lowestCommonAncestorRecursive(root.right, p, q)

    if left is None:
        return right
    elif right is None:
        return left
    else:
        return root


# O(n), O(n)

def lowestCommonAncestorIterative(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    # Stack for tree traversal
    stack = [root]

    # Dictionary for parent pointers (child is key and parent is value)
    parent = {root: None}

    # Iterate until we find both the nodes p and q
    while p not in parent or q not in parent:

        node = stack.pop()

        # While traversing the tree, keep saving the parent pointers.
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)

    # Ancestors set() for node p.
    ancestors = set()

    # Process all ancestors for node p using parent pointers.
    while p:
        # add current node/ ancestor of p
        ancestors.add(p)
        # get the ancestor of current child p (remember child is key and parent is value in parent dictionary)
        p = parent[p]

    # keep getting the ancestor of q
    # The first ancestor of q which appears in
    # p's ancestor set() is their lowest common ancestor.
    while q not in ancestors:
        q = parent[q]
    return q


# definition of binary tree
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)

# print(lowestCommonAncestorRecursive(root, Node(7), Node(4)).val)

n1 = root.left.right.left
n2 = root.left.right.right

print(lowestCommonAncestorIterative(root, n1, n2).val)


## another method

# this is the advanced implementation which checks if both the
# values are present in the tree, if either one or both of the values are not present
# it will return None
# if duplicate nodes are present one in left and another one in right then root node will be returned

# O(n), O(n)

def find(root, v):
    """
    find the value in tree
    :param root: TreeNode
    :param v: val[int]
    :return: boolean

    """

    if root is None:
        return None

    if root.val == v or find(root.left, v) or find(root.right, v):
        return True

    return False


def findLCA(root, n1, n2, v):
    """
    finds the lca
    :param root: TreeNode
    :param n1: val[int]
    :param n2: val[int]
    :param v: List
    :return: TreeNode

    """
    if root is None:
        return None

    if root.val == n1:
        v[0] = True
        return root

    if root.val == n2:
        v[1] = True
        return root

    left_lca = findLCA(root.left, n1, n2, v)
    right_lca = findLCA(root.right, n1, n2, v)

    # one key is present in left sub-tree and other in right sub-tree then lca is root
    if left_lca and right_lca:
        return root

    if left_lca is not None:
        return left_lca
    else:
        return right_lca


def findLCAinBTree(root, n1, n2):
    """
    find and returns the lca if both values are present otherwise returns None
    :param root:TreeNode
    :param n1: val[int]
    :param n2: val[int]
    :return: TreeNode

    """
    v = [False, False]

    lca = findLCA(root, n1, n2, v)

    print("LCA: " + str(lca.val))

    # returns lca if both n1 and n2 are present in the tree
    if (v[0] and v[1]) or (v[0] and find(lca, n2)) or (v[1] and find(lca, n1)):
        return lca

    return None


print(findLCAinBTree(root, 7, 4).val)
