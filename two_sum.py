# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_nums = {}
        for index, num in enumerate(nums):
            all_nums[num] = index
        for index, num in enumerate(nums):
            num2 = target - num
            if num2 in all_nums.keys() and index != all_nums[num2]:
                return [index, all_nums[num2]]
        return []