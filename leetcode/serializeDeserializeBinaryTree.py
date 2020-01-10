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
