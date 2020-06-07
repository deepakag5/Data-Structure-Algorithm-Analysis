# Time: O(N)
# Space: O(1)

def twoSum(numbers, target):
    # base case
    if target <= numbers[0]:
        return [-1, -1]

    low, high = 0, len(numbers) - 1

    while low < high:
        sum_nums = numbers[low] + numbers[high]
        if sum_nums == target:
            return [low, high]  # use [low+1, high+1] if return indices are supposed to be non-zero based
        elif sum_nums < target:
            low += 1
        else:
            high -= 1

    return [-1, -1]
