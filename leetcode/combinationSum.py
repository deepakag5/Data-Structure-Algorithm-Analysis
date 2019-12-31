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