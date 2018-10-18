#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 乘最多水的容器.py
"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
画 n 条垂直线，使得垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
使得它们与 x 轴共同构成的容器可以容纳最多的水。

注意：你不能倾斜容器，n 至少是2。
"""
"""
思路: 利用两个指针, 一个指向头, 一个指向尾. 其中指向短的那个向中间移动,
因为长的向中间移动面积一定不会变大(取最小的为高),
所以考虑短的向中间移动, 直到两个指针相遇
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxS = 0
        while i < j:
            if height[i] < height[j]:
                temS = height[i] * (j - i)
                if temS > maxS:
                    maxS = temS
                i += 1
            else:
                temS = height[j] * (j - i)
                if temS > maxS:
                    maxS=temS
                j -= 1
        return maxS


def main():
    sol=Solution()
    h=[1, 1]
    print(sol.maxArea(h))


if __name__ == '__main__':
    main()
