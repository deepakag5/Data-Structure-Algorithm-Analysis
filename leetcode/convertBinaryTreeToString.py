def binaryTreeToString(root):
    if root is None:
        return False

    char_str = str(root.val)

    if root.left is not None and root.right is not None:
        char_str += '(' + binaryTreeToString(root.left) + ')'

    if root.right is not None:
        char_str += '(' + binaryTreeToString(root.right) + ')'

    return char_str
