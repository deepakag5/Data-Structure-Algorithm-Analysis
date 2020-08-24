# Time: O(N) since each node is processed exactly once.
# Space: O(N)


def isSymmetric(root):
    def isMirror(t1, t2):
        if t1 is None and t2 is None:
            return True

        if t1 is None or t2 is None:
            return False

        return t1.val == t2.val and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

    return isMirror(root, root)


def isSymmetricIterative(root):
    queue = [root, root]

    while queue:
        t1, t2 = queue.pop(), queue.pop()

        if t1 is None and t2 is None:
            continue

        if t1 is None or t2 is None:
            return False

        if t1.val != t2.val:
            return False

        queue.append(t1.right)
        queue.append(t2.left)
        queue.append(t1.left)
        queue.append(t2.right)

    return True
