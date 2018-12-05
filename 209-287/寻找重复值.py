#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 寻找重复值.py
"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n^2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
"""
"""
思路：利用所有的数字都是1-n之间的整数 最大值为len(nums)-1 将数组理解为一个链表 每个位置储存下一个位置的索引 根据题意 环必定存在
1 -> 3 -> 2 -> 2
"""
__author__ = 'Aiyane'


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0],nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[fast]
        
        return nums[slow]
