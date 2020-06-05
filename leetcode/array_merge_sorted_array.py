# Brute Force

# Time: O((n+m) log(n+m))
# Space: O(1)


def mergeSortedArr(nums1, m, nums2, n):
    nums1[:] = sorted(nums1[:m] + nums2)


# Time: O(n+m)
# Space: O(m)

def mergeSortedArr1(nums1, m, nums2, n):
    nums1_copy = nums1[:m]
    nums1[:] = []

    p1, p2 = 0, 0

    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1

    if p1 < m:
        nums1[p1 + p2:] = nums1_copy[p1:]
    if p2 < n:
        nums1[p1 + p2:] = nums2[p2:]


# Time: O(n+m)
# Space: O(1)

def mergeSortedArr2(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1

    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

    nums1[:p2 + 1] = nums2[:p2 + 1]
