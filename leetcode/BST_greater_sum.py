def bsttoGSTRecursive(root):
    def revinorder(node, val):
        if not node:
            return val
        node.val += revinorder(node.right, val)
        return revinorder(node.left, node.val)

    revinorder(root, 0)

    return root


# similar to inorder iterative but of course in reverse order
def bsttoGSTIterative(root):
    sum_nodes = 0
    node = root
    stack = []

    while stack or node:
        # here instead of if we used while as we want to traverse all nodes in right first
        while node:
            stack.append(node)
            node = node.right

        node = stack.pop()
        # assign
        node.val += sum_nodes
        # accumulate
        sum_nodes = node.val
        # traverse
        node = node.left

    return root
