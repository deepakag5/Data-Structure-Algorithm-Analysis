# Time: O(N)
# Space: O(N)


def PostOrderRecursive(root):
    if not root:
        return []

    output = []

    def dfs(root):
        dfs(root.left)
        dfs(root.right)
        output.append(root.val)

    return output


def postOrderTraversalDFS(root):
    if root is None:
        return []

    stack, output = [root], []

    while stack:
        node = stack.pop()
        output.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # we are adding in order root->right->left in output list
    # (because right is added after left on stack it will get popped and added to output list)
    # thus we need to reverse the output list for our postorder traversal (left->right->root)

    return output[::-1]


def PostOrderIterative(root):
    if root is None:
        return False

    stack = []

    visited = set()

    if root is not None:
        stack.append(root)

    while len(stack) > 0:
        node = stack.pop()

        if node in visited:
            print(node.val)
        else:
            visited.add(node)
            stack.append(node)

            if node.right is not None:
                stack.append(node.right)

            if node.left is not None:
                stack.append(node.left)



