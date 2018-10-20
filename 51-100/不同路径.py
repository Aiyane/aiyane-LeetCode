#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 不同路径.py
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
https://leetcode-cn.com/problems/unique-paths/
例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:
输入: m = 3, n = 2
输出: 3

解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:
输入: m = 7, n = 3
输出: 28
"""
"""
思路：以下是最优解，看不懂？？
def uniquePaths(m, n):
    res = 1
    for i in range(m, m+n-1):
        res *= i
        res /= i-m+1
    return int(res)
一般考虑用动态规划求解，将坐标位置的个数保存起来。转移方程考虑：一个坐标只有两个方向移动，右或者下。所以将两个方向的加起来就行了。
"""
__author__ = 'Aiyane'


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.tem = {}
        return self.getRes(m-1, n-1)

    def getRes(self, m, n):
        if (m, n) in self.tem:
            return self.tem[(m, n)]
        if m == 0 and n == 0:
            return 1
        num = 0
        if m > 0:
            num = self.getRes(m-1, n)
        if n > 0:
            num += self.getRes(m, n-1)
        self.tem[(m, n)] = num
        return num

if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePaths(3,2))
