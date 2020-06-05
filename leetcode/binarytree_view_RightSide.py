# Time: O(N)
# Space: O(D)  where D is diameter of B-Tree

# BFS: Using Two Queues

from collections import deque


def rightSideView(root):
    if not root:
        return []

    # push the root to the next level
    next_level = deque([root, ])
    # to store rightmost node values
    rightside = []

    # perform a bfs until tree has next level
    while next_level:
        # make next level as current level
        curr_level = next_level
        # remove the node from next level
        next_level = deque()

        while curr_level:
            # perform a popleft (as we want the right most element to
            # be popped last, as once this loop exits, we will add it to rightside)
            node = curr_level.popleft()

            # if there is left or right child add it to curr level to be popped
            if node.left:
                curr_level.append(node.left)
            if node.right:
                curr_level.append(node.right)

        # here the above loop has exited and we got our desired right most node
        rightside.append(node.val)

    return rightside
