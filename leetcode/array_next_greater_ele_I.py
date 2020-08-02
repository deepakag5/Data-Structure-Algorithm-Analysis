# Time: O(m*n)
# Space: O(m)


def nextGreaterElement(nums1, nums2):
    if not nums1:
        return []

    hash_map = {}
    out_list = []

    for i in range(len(nums2)):
        hash_map[nums2[i]] = i

    for item in nums1:
        idx = hash_map[item]

        if idx < len(nums2) - 1:
            for i in range(idx + 1, len(nums2)):
                if item < nums2[i]:
                    out_list.append(nums2[i])
                    break
            else:
                out_list.append(-1)

        else:
            out_list.append(-1)

    return out_list
