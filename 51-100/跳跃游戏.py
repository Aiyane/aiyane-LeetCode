#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 跳跃游戏.py
"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。

示例 2:
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""
"""
思路：可以参考 1-50 中的跳跃游戏2
"""
__author__ = 'Aiyane'


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums) - 1
        j = m = nums[0]
        while j < l:
            for i, num in enumerate(nums[:j+1]):
                m = max(i + num, m)
            if j == m < l:
                return False
            j = m
        return True

def main():
    sol = Solution()
    print(sol.canJump([2,3,1,1,4]))
    print(sol.canJump([3,2,1,0,4]))

if __name__ == '__main__':
    main()