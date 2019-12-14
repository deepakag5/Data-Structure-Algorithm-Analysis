def PreOrderRecursive(root):
    if root:
        print(root.val)

        printPreOrder(root.left)

        printPreOrder(root.right)


def PreOrderIterative()
