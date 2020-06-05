# Time: O(n+m)
# Space: O(n+m)


def intersectionOfTwoArr(nums1, nums2):
    # edge case
    if len(nums1) == 0 or len(nums2) == 0:
        return []

    return list(set(nums1) & set(nums2))
