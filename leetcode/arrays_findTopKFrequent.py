# O (N log N)
# O (N)

from collections import Counter


def findtopK(words, k):
    count = Counter(words)
    candidates = list(count.keys())
    candidates.sort(key=lambda w: (-count[w], w))
    return candidates[:k]


# O (N log k) where N is the length of words.
# We count the frequency of each word in O(N)O(N) time, then we add N words to the heap,
# each in O(log k) time. Finally, we pop from the heap up to k times

# O (N)

import heapq


def findtopK_heap(words, k):
    count = Counter(words)
    return heapq.nsmallest(k, count.keys(), key=lambda w: (-count[w], w))
