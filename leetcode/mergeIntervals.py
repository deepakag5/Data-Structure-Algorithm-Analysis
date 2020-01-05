def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = []

    for i in intervals:
        if not merged or merged[-1][-1] < i[0]:
            merged.append(i)
        else:
            merged[-1][-1] = max(merged[-1][-1], i[-1])

    return merged
