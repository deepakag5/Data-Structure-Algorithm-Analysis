# Brute Force  - O(n^2), O(1)

def TwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]

# Optimize using dict - O(n), O(1)

def TwoSumHash(nums, target):
   nums_dict = {}

   for i in range(len(nums)):
       nums_dict[nums[i]] = i

   for i in range(len(nums)):
        complement = target - nums[i]

        if complement in nums_dict and nums_dict.get(complement)!=i:
            return [i, nums_dict.get(complement)]

