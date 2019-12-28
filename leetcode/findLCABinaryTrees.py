def lowestCommonAncestor(root, p, q):
     if root is None:
         return None

     if root.val == p.val or root.val == q.val:
         return root

     left = lowestCommonAncestor(root.left, p, q)
     right = lowestCommonAncestor(root.right, p, q)

     if left is None:
         return right

     if right is None:
         return left

     return root



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


print(lowestCommonAncestor(root, Node(7), Node(4)).val)

























## another method from geeksforgeeks

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

    print("LCA: "+str(lca.val))

    # returns lca if both n1 and n2 are present in the tree
    if (v[0] and v[1]) or (v[0] and find(lca, n2)) or (v[1] and find(lca, n1)):
        return lca

    return None


print(findLCAinBTree(root, 7, 4).val)