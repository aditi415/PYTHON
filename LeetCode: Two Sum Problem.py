#---Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.    You may assume that each input would have exactly one solution, and you may not use the same element twice.



def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# Examples
print(twoSum([2,7,11,15,4,5], 9))   # [0,1]
print(twoSum([3,2,4], 6))           # [1,2]
print(twoSum([3,3], 6))             # [0,1]
