# O(S*T)

def isSubtree(s, t):
    """
      :param s: tree
      :param t: find if this is subtree of s
    :return: bool
    """

    def areIdentical(s, t):
        if (s is None and t is not None) or (s is not None and t is None):
            return False

        elif s is None and t is None:
            return True

        if s.val == t.val:
            if areIdentical(s.left, t.left) and areIdentical(s.right, t.right):
                return True
            else:
                return False

        if areIdentical(s, t):
            return True
        if s is None:
            return False

        return isSubtree(s.left, t) or isSubtree(s.right, t)
