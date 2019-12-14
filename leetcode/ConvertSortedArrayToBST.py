# importing Node class from our bianrytree.py module
from binarytree import Node


def sortedArrayBSTRecursive(arr):
    if not arr:
        return False

    mid = len(arr) // 2

    root = Node(arr[mid])

    root.left = sortedArrayBSTRecursive(arr[:mid])
    root.right = sortedArrayBSTRecursive(arr[mid + 1:])

    return root


def sortedArrayBSTIterative(arr):
    left = 0
    right = len(arr)
    mid = left + right // 2

    root = Node(arr[mid])
    stack = [(root, left, mid, right)]

    while stack:
        node, left, mid, right = stack.pop()

        if left != mid:
            node.left = Node(arr[(left + mid) // 2])
            stack.append((node.left, left, (left + mid) // 2, mid))

        if right != mid + 1:
            node.right = Node(arr[(mid + right + 1) // 2])
            stack.append((node.right, mid, (mid + right + 1) // 2, right))

    return root
