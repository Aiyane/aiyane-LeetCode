#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 四的幂.py
"""
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？
"""
__author__ = 'Aiyane'


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
        return 4**round(math.log(4, n)) == n
