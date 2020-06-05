# Time: O(n) in both serialization and deserialization functions, we visit each node exactly once,
# where N is the number of nodes, i.e. the size of tree.

# Space : O(n) in both serialization and deserialization functions, we keep the entire tree,
# either at the beginning or at the end,

def serialize(root):
    def rserialize(root, string):
        if root is None:
            string += "None,"
        else:
            string += str(root.val) + ","
            string = rserialize(root.left, string)
            string = rserialize(root.right, string)

        return string

    return rserialize(root, "")


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def deserialize(data):
    def rdeserialize(l):
        if l[0] == None:
            l.pop(0)
            return None

        root = Node(l[0])
        l.pop(0)

        root.left = rdeserialize(l)
        root.right = rdeserialize(l)

        return root

    data_list = data.split(',')
    root = deserialize(data_list)

    return root
