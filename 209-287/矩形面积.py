#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 矩形面积.py
"""
在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。
https://leetcode-cn.com/problems/rectangle-area/

示例:
输入: -3, 0, 3, 4, 0, -1, 9, 2
输出: 45
说明: 假设矩形面积不会超出 int 的范围。
"""
__author__ = 'Aiyane'


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        return (C - A)*(D - B) + (G - E)*(H - F) - max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
