# Time O(N+M)
# Space: O(min(N+M))  to store the result


def intersection_use_hm(nums1, nums2):
    # base case
    if len(nums1) == 0 or len(nums2) == 0:
        return []

    # to store the array with smaller size (reduce memory footprint)
    hash_table = {}
    result = []

    if len(nums1) <= len(nums2):
        # get count of each element in smaller array
        for item in nums1:
            hash_table[item] = hash_table.get(item, 0) + 1
        # iterate over larger array and if element is in hash map
        # and it's count>0 then decrease its count in hashmap and
        # add that number to result set
        for item in nums2:
            if item in hash_table and hash_table[item] > 0:
                hash_table[item] -= 1
                result.append(item)
    else:
        # swap if second array is smaller than first
        return intersection_use_hm(nums2, nums1)

    return result


# Time O((N log N)+(M log M))
# Space: O(1)  (we can store the result in one of the arrays as well and return till k)

def intersection_use_sort(nums1, nums2):
    if len(nums1) == 0 or len(nums2) == 0:
        return []

    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    # result = []

    i, j, k = 0, 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            nums1[k] = nums1[i]
            #result.append(nums1[i])
            i += 1
            j += 1
            k += 1

    return nums1[:k]

# Follow-up Questions

# What if the given array is already sorted? How would you optimize your algorithm?
# We can use Approach 2 dropping the sort of course. It will give us linear time
# and constant memory complexity.

# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# Approach 1 is a good choice here as we use a hash map for the smaller array.

# What if elements of nums2 are stored on disk, and the memory is limited such that you
# cannot load all elements into the memory at once?
# If nums1 fits into the memory, we can use Approach 1 to collect counts for nums1 into a hash map.
# Then, we can sequentially load and process nums2.

# If neither of the arrays fit into the memory, we can apply some partial processing strategies:

# Split the numeric range into subranges that fits into the memory. Modify Approach 1 to collect counts
# only within a given subrange, and call the method multiple times (for each subrange).

# Use an external sort for both arrays. Modify Approach 2 to load and process arrays sequentially.
