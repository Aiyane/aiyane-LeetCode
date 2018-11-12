#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 直线上最多的点数.py
"""
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:
输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

示例 2:
输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
"""
"""
思路：没有特别好的方法，暴力求解，注意浮点数相除有误差，使用最大公约数。
"""
__author__ = 'Aiyane'


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def commonDivisor(self, num1, num2):
        return num1 if num2 == 0 else self.commonDivisor(num2, num1 % num2)

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        maxPoint = 0
        for i, point in enumerate(points):
            table = {}
            same = maxTable = 0
            for j, oth_point in enumerate(points):
                if oth_point.x == point.x and oth_point.y == point.y:
                    same += 1
                elif i != j:
                    common = self.commonDivisor(oth_point.y - point.y, oth_point.x - point.x)
                    a = ((oth_point.y - point.y) // common, (oth_point.x - point.x) // common) if oth_point.x != point.x else None
                    table[a] = table[a] + 1 if a in table else 1
                    maxTable = max(maxTable, table[a])
            maxTable += same
            maxPoint = max(maxPoint, maxTable)
        return maxPoint
