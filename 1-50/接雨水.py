#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 接雨水.py
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
https://leetcode-cn.com/problems/trapping-rain-water/
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1
输出: 6
"""
"""
思路：将每次下降的楼的序号保存起来，考察上升楼
"""
__author__ = 'Aiyane'
import profile


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        old = ret = 0
        cs = []
        for i, ch in enumerate(height):
            if ch < old:
                cs.append(i-1)

            else:
                while cs and old < ch:
                    ret += (i - cs[-1] - 1)*(min(height[cs[-1]], ch)-old)
                    old = height[cs.pop()] if height[cs[-1]] < ch else height[cs[-1]]

            old = ch
        return ret

def main():
    sol = Solution()
    print(sol.trap([2,0,2]))
    print(sol.trap([5,5,1,7,1,1,5,2,7,6]))
    print(sol.trap([4,2,0,3,2,5]))
    print(sol.trap([2,1,0,2]))
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

if __name__ == '__main__':
    profile.run('main()')