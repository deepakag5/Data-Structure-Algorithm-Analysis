def merge(intervals):
    # base case
    if not intervals:
        return []
    # sort the list on basis of first value in each sub-list
    intervals.sort(key=lambda x: x[0])
    merged = []

    for i in intervals:
        # if the list of merged intervals is empty
        # or if the current interval does not overlap with the previous,
        # simply append it.
        if not merged or merged[-1][-1] < i[0]:
            merged.append(i)
        # otherwise, there is overlap,
        # so we merge the current and previous intervals
        # by getting max in last value of the sub-lists
        else:
            merged[-1][-1] = max(merged[-1][-1], i[-1])

    return merged
