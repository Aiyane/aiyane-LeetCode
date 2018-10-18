# -*- coding: utf-8 -*-
#!/usr/bin/python3
# File Name: 两数之和.py
# Created Time: Sun 29 Apr 2018 10:38:08 PM CST
"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""
"""
思路: 通过字典来进行速度上的提升
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_map = {}
        for i in range(len(nums)):
            if nums[i] in my_map:
                return [my_map[nums[i]], i]
            my_map[target - nums[i]] = i


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([3, 2, 4], 6))

