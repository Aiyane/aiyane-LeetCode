#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 最接近的三数之和.py
"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""
"""
思路: 固定第一个数, 考察后两个数, 后两个数从一个头指针与一个尾指针移动来考察, 观察相加是否为目标
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        retnum = 10000
        ret = 0
        nums.sort()
        i = 0
        n_len = len(nums)
        while i < n_len - 2:
            j = i + 1
            k = n_len - 1
            while j < k:
                now = nums[i] + nums[j] + nums[k]
                if now == target:
                    return target
                elif now < target:
                    if abs(now - target) < retnum:
                        retnum = abs(now - target)
                        ret = now
                    j += 1
                else:
                    if abs(now - target) < retnum:
                        retnum = abs(now - target)
                        ret = now
                    k -= 1
            i += 1
        return ret
