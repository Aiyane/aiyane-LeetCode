#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 三数之和.py
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
"""
思路: 固定第一个数, 考察后两个数, 后两个数从一个头指针与一个尾指针移动来考察, 观察相加是否为目标
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # 先将列表按由小到大排序
        res = []
        i = 0
        n_len = len(nums)
        while i < n_len - 2:

            # 优化1: 第一个数大于0直接不用考察
            if nums[i] > 0:
                break

            # 优化2: 如果之前考察过这个数直接跳过
            if 0 <= i-1 and nums[i-1] == nums[i]:
                i += 1
                continue

            target = 0 - nums[i]
            j = i + 1
            k = n_len - 1
            while 1:
                now = nums[j] + nums[k]
                if now == target:
                    res.append([nums[i], nums[j], nums[k]])

                    # 将相等的数跳过
                    while j < k and nums[j] == nums[j+1]:
                        j += 1

                    # 将相等的数跳过
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    # 由于这是等于0内部, 所以改变一个指针就不等于0了, 所以直接改变2个指针考察
                    j += 1
                    k -= 1
                elif now > target:
                    k -= 1
                else:
                    j += 1

                    # 优化3: 如果前两数与下一个数相加大于1不用考察了
                    if j >= k or nums[i] + nums[j] + nums[j+1] > 0:
                        break
            i += 1
        return res
