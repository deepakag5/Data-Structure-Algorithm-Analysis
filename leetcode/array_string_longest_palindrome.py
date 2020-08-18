# Time: O(n)
# Space: O(n)


def longest_palin(s):
    if len(s) <= 1:
        return len(s)

    hash_map = {}

    for char in s:
        hash_map[char] = hash_map.get(char, 0) + 1

    max_len = 0
    met_odd = True

    for v in hash_map.values():
        if v % 2 == 0:
            max_len += v
        else:
            # if we encounter an odd val then add it to total
            # but from next onwards we add only even number of chars
            # for those odd chars
            if met_odd:
                max_len += v
                met_odd = False
            else:
                max_len += (v - 1)

    return max_len
