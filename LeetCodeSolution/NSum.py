

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
        """
        # 算法思想: 先把每个int的index都统计起来
        # 循环num，查找target-num是否在统计表中
        # 空间换时间, 时间复杂度O(n) 空间复杂度O(n)
        num_index = {}
        for index,num in enumerate(nums):
            if num in num_index:
                num_index[num].append(index)
            else:
                num_index[num] = [index]

        for index,num in enumerate(nums):
            _aim = target - num
            if not num_index[num]:
                continue
            if _aim in num_index and num_index[_aim] and num_index[_aim][0] != index:
                return [index,num_index[_aim].pop(0)]

        return []

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Given an array nums of n integers,
        are there elements a,b,c in nums such that a+b+c=0?
        Find all unique triplets in the array which gives the sum os zero.
        """
        