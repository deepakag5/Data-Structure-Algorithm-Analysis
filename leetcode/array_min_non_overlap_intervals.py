def minNonOverlapIntervals(intervals):
    if len(intervals) == 0:
        return 0

    nonOverlapInt = 1
    prevEnd = intervals[0][1]

    for i in range(1, len(intervals)):
        curStart, curEnd = intervals[i][0], intervals[i][1]
        if curStart >= prevEnd:
            nonOverlapInt += 1
            prevEnd = curEnd

    return len(intervals) - nonOverlapInt
