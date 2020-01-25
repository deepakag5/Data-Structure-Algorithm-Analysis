# k is average length of each solution, and we need O(k) time to copy new linkedlist when we get one combination.
# For example, given int[] arr = {2, 3, 4, 5, 6} and target is 10 and each element can be used for MORE than once.
# Actually, it is same with the problem: given int[] arr = {2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6}, and target 10,
# each element can be used for ONLY one time, which is the same description of Combination Sum II.
# And you must find that for the new array, each element E, which is smaller than target, will expand to ceil(target/E).
# Assume the new array has length n', we can get the time complexity which is O(k * 2 ^ n')

def combSum(candidates, target):
    res = []

    candidates.sort()

    def dfs(target, index, path):
        if target<0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(candidates)):
            dfs(target-candidates[i], i, path+[candidates[i]])

    dfs(target, 0, [])

    return res



def combinationSumOptimized(candidates, target):
        candidates.sort()
        def combinSum(sortedCandidates, target):
            if sortedCandidates[0] > target:
                return []
            results = []
            for i, n in enumerate(sortedCandidates):
                if n < target:
                    part_results = combinSum(sortedCandidates[i:], target - n)
                    for part in part_results:
                        results.append([n] + part)
                elif n == target:
                    results.append([n])
                    break
                else:
                    break
            return results
        return combinSum(candidates, target)