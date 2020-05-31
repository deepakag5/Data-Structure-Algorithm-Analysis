# Time: O(N)
# Space: O(D)  where D is diameter of B-Tree

# BFS: Using Two Queues (Same as right side view with only change
# that we add right child first to the curr level then left child)

from collections import deque


def rightSideView(root):
    if not root:
        return []

    # push the root to the next level
    next_level = deque([root, ])
    # to store rightmost node values
    leftside = []

    # perform a bfs until tree has next level
    while next_level:
        # make next level as current level
        curr_level = next_level
        # remove the node from next level
        next_level = deque()

        while curr_level:
            # perform a popleft
            node = curr_level.popleft()

            # as we want the left most element to
            # be popped last, we are adding right element first and then left child
            # as once this loop exits, we will add it to leftside)
            # if there is left or right child add it to curr level to be popped
            if node.right:
                curr_level.append(node.right)
            if node.left:
                curr_level.append(node.left)

        # here the above loop has exited and we got our desired left most node
        leftside.append(node.val)

    return leftside
