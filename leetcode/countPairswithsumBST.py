def countPairs(root, given_sum):
    # two stacks to store nodes for forward and backward iterator
    stack1 = []
    stack2 = []

    node = root

    while node is not None:
        stack1.append(node)
        node = node.left

    node = root

    while node is not None:
        stack2.append(node)
        node = node.right

    total_pairs = 0

    while stack1[-1] != stack2[-1]:
        v1 = stack1[-1].val
        v2 = stack2[-1].val

        if (v1 + v2) == given_sum:
            total_pairs += 1

        if (v1 + v2) <= given_sum:
            node = stack1[-1].right
            stack1.pop()
            while node is not None:
                stack1.append(node)
                node = node.left
        else:
            node = stack2[-1].left
            stack2.pop()
            while node is not None:
                stack2.append(node)
                node = node.right

    return total_pairs
