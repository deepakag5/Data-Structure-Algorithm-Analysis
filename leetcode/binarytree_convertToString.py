def binaryTreeToStringRecursive(root):
    if root is None:
        return False

    char_str = str(root.val)

    if root.left is not None and root.right is not None:
        char_str += '(' + binaryTreeToStringRecursive(root.left) + ')'

    if root.right is not None:
        char_str += '(' + binaryTreeToStringRecursive(root.right) + ')'

    return char_str
