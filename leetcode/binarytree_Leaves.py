def findLeavesRecursive(root):
    """
    :param root: TreeNode
    :return: List[List]
    """
    # create result list to hold the leaves at each height/depth
    res_list = []

    # do a dfs seach
    def find_height(node):
        if node is None:
            return 0

        # get the max height of the tree
        height = max(find_height(node.left), find_height(node.right)) + 1
        # print(height)

        # if result list has less items than height append for holding items for that height
        if len(res_list) < height:
            # print("in if")
            res_list.append([])

        # add node value to its level
        # remember level is height -1 (root level is considered as 0)
        res_list[height - 1].append(node.val)
        # print(res_list)

        # this is collected by recursive calls made at line 15
        return height

    find_height(root)

    # print(res_list)
    return res_list


def findLeavesIterative(root):
    """
    :param root: TreeNode
    :return: List[List]
    """
    # edge case
    if root is None:
        return None

    # to hold the leaves as list of lists
    res_list = []

    # find the height and accordingly put node values (those at same height will be put together)
    def find_height(node):
        # if node is not present return
        if node is None:
            return

        # put the current depth and node on stack
        stack = [(1, node)]

        depth = 0

        while stack:
            current_depth, node = stack.pop()

            if node:
                # depth starts with 1 (value of current depth !)
                depth = max(current_depth, depth)
                stack.append((current_depth + 1, node.right))
                stack.append((current_depth + 1, node.left))

                # if list length is less then depth which means that
                # add a list in result list only if there are are more levels
                # remember depth starts with 1 while list starts with 0 that's why <
                if len(res_list) < depth:
                    res_list.append([])

                # because depth starts with 1 but list starts with 0 index
                res_list[depth - 1].append(node.val)

    find_height(root)

    # we need to reverse the list of list as it's has elements
    # from root, then second level then leaf level
    # also if we need only the leaf nodes we can return
    # either res_list[-1] or res_list[::-1][0]
    return res_list[::-1]
