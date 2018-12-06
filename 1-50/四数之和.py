#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 四数之和.py
"""

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：
答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
"""
四路：参考三数之和。
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n_len = len(nums)
        nums.sort()
        i = 0
        res = []
        while i < n_len - 3:
            if sum(nums[i:i+4]) > target:
                break

            if 0 <= i-1 and nums[i-1] == nums[i]:
                i += 1
                continue

            j = i + 1
            while j < n_len - 2:
                if nums[i] + sum(nums[j:j+3]) > target:
                    break

                if i+1 <= j-1 and nums[j-1] == nums[j]:
                    j += 1
                    continue

                k = j+1
                z = n_len - 1
                tar = target - nums[i] - nums[j]
                while k < z:
                    now = nums[k] + nums[z]
                    if now == tar:
                        res.append([nums[i], nums[j], nums[k], nums[z]])
                        while k < z and nums[k] == nums[k+1]:
                            k += 1
                        while k < z and nums[z] == nums[z-1]:
                            z -= 1
                        k += 1
                        z -= 1
                    elif now > tar:
                        z -= 1
                    else:
                        k += 1
                j += 1
            i += 1
        return res
