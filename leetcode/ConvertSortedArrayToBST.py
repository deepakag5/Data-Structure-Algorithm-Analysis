# importing Node class from our bianrytree.py module
from binarytree import Node


def sortedArrayBSTRecursive(arr):
    if not arr:
        return False

    mid = len(arr) // 2

    node = Node(arr[mid])

    node.left = sortedArrayBSTRecursive(arr[:mid])
    node.right = sortedArrayBSTRecursive(arr[mid + 1:])

    return node
