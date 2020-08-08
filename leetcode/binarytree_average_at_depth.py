# Approach 1 : DFS
# Time: O(n) -- we must traverse all the elements in the tree to calculate average at each level
# Space: O(n) -- we are storing all tree elements in the hash_map


class Node(object):
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(4)
root.left.left = Node(7)
root.left.right = Node(5)
root.right.right = Node(9)


def collect(node, hash_map, depth=0):
    if not node:
        return None

    if depth not in hash_map:
        hash_map[depth] = []

    hash_map[depth].append(node.val)

    collect(node.left, hash_map, depth + 1)
    collect(node.right, hash_map, depth + 1)


def average_by_level(node):
    hash_map = {}

    collect(node, hash_map)

    result = []

    print(hash_map)

    for level in hash_map:
        nums = hash_map[level]
        avg = sum(nums) / len(nums)
        result.append(avg)

    return result


# DFS space optimized version
# Time: O(n) -- we must traverse all the elements in the tree to calculate average at each level
# Space: O(k) -- where k is the number of levels (we are storing only the total sum and count for each level)


def collect_opt(node, hash_map, depth=0):
    if not node:
        return None

    if depth not in hash_map:
        hash_map[depth] = (node.val, 1)
    else:
        val, count = hash_map[depth]
        val += node.val
        count += 1
        hash_map[depth] = (val, count)

    collect_opt(node.left, hash_map, depth + 1)
    collect_opt(node.right, hash_map, depth + 1)


def average_opt(node):
    hash_map = {}

    collect_opt(node, hash_map)

    result = []

    for level in hash_map:
        level_sum, count = hash_map[level]
        avg = level_sum / count
        result.append(avg)

    return result
