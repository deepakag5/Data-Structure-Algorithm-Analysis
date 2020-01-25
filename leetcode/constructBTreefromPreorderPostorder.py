# Time O(N^2), as we are iterating over copies of both pre and post sub-arrays
# Space O(N^2), passing copies of both pre and post sub-arrays

def constructTreeRecursive(preorder, postorder):
    """
    :param preorder: list
    :param postorder: list
    :return: TreeNode
    """
    if not postorder:
        return None
    elif len(postorder) == 1:
        return Node(preorder.pop(0))
    else:
        root = Node(preorder.pop(0))
        # as we have already popped off root in previous step
        # in first pass below - we are getting left subtree root - preorder[1] from original array
        pos = postorder.index(preorder[0])
        # In first pass of recursive call root and left, right sub trees will get identified
        # In successive calls left and right childs will be assigned
        root.left = constructTreeRecursive(preorder, postorder[:pos + 1])
        root.right = constructTreeRecursive(preorder, postorder[pos + 1:-1])
        return root


# Time O(N), here the problem has been divided into two sub problems a=2(to compute left and right subtree)
# and the size of each sub-problem is half of the initial problem, b=2,  O(N^logb(a)) -- log2(2)=1, O(N) -- master theorem case - 1
# Space O(N), as we are passing only the indexes for both pre and post


def constructTreeRecursiveOptimized(preorder, postorder):
    """
    :param preorder: list
    :param postorder: list
    :return: TreeNode
    """
    postorder_map = {}
    for i, num in enumerate(postorder):
        postorder_map[num] = i

    def constructTree(prestart, preend, poststart, postend):
        if prestart > preend:
            return None
        elif prestart == preend:
            return Node(preorder[prestart])
        else:
            # find the root node
            root = Node(preorder[prestart])
            # find the left sub tree root val
            left_val = preorder[prestart + 1]
            # find the length of left sub tree
            left_len = postorder_map[left_val] - poststart + 1
            # assign value to left and right sub trees
            # In first pass of recursive call root and left, right sub trees will get identified
            # In successive calls left and right childs will be assigned
            root.left = constructTree(prestart + 1, prestart + left_len, poststart, poststart + left_len - 1)
            root.right = constructTree(prestart + left_len + 1, preend, poststart + left_len, postend - 1)
            return root

    return constructTree(0, len(preorder) - 1, 0, len(postorder) - 1)


# Time O(N), as we iterate both pre index and post index only once.
# Space O(height), depending on the height of constructed tree

def constructTreeIterative(preorder, postorder):
    """
    :param preorder: list
    :param postorder: list
    :return: TreeNode
    """
    stack = [Node(preorder[0])]
    posIndex = 0
    for pre_val in preorder[1:]:
        node = Node(pre_val)
        while stack[-1].val == postorder[posIndex]:
            # this loop runs when the last value at stack matches the postorder value at posindex
            # which means when there is no leaf node anymore so we must pop
            stack.pop()
            posIndex += 1
        if not stack[-1].left:
            # this loop runs to attach left child
            stack[-1].left = node
        else:
            # this loop runs to attach right child
            stack[-1].right = node
        stack.append(node)
        # return root node ref
    return stack[0]