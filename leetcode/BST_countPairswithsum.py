def countPairs(root, given_sum):
    """
    :param root: TreeNode
    :param given_sum: int
    :return: int
    """

    # two stacks to store nodes for forward and backward iterator
    stack1 = []
    stack2 = []

    # initialize forward iterator
    node = root

    while node is not None:
        stack1.append(node)
        node = node.left

    # initialize backward iterator
    node = root

    while node is not None:
        stack2.append(node)
        node = node.right

    total_pairs = 0

    # two pointers iterate until they point to the same node
    while stack1[-1] != stack2[-1]:

        # Variables to store the value of the nodes
        # current iterators are pointing to
        v1 = stack1[-1].val
        v2 = stack2[-1].val

        # if we find a pair that's equivalent to
        # desired sum increment the count
        if (v1 + v2) == given_sum:
            total_pairs += 1

        # moving forward iterator
        if (v1 + v2) <= given_sum:
            node = stack1[-1].right
            stack1.pop()
            while node is not None:
                stack1.append(node)
                node = node.left
        # moving backward iterator
        else:
            node = stack2[-1].left
            stack2.pop()
            while node is not None:
                stack2.append(node)
                node = node.right

    # return total pairs found
    return total_pairs
