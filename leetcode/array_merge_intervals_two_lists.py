# Time Complexity: Best case : O(m+n)
# Space Complexity - O(m+n) for holding the results


def merge(list1, list2):
    # base case
    if not list1:
        return list2
    if not list2:
        return list1

    # first we need to merge both lists in sorted order (on basis of first element) so that we can then merge intervals
    i, j = 0, 0
    merged_list = []

    while i < len(list1) and j < len(list2):
        if list1[i][0] <= list2[j][0]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # if one list is greater in length than other list then
    # we need to append rest of the elements from that list at the end
    if i < len(list1):
        merged_list.extend(list1[i:])

    if j < len(list2):
        merged_list.extend(list2[j:])

    # now we can just iterate over this merged list and combine the intervals
    combined_intervals = []

    for item in merged_list:
        if not combined_intervals or combined_intervals[-1][-1] < item[0]:
            combined_intervals.append(item)
        else:
            combined_intervals[-1][-1] = max(combined_intervals[-1][-1], item[-1])

    return combined_intervals