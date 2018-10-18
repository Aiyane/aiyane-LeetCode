#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name: 反转整数.py
# Created Time: Tue 01 May 2018 06:18:28 PM CST
"""
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21

注意:
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""
"""
思路: 直接做就好, python就是这么强大!
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            s = int(str(x)[1:][::-1])
            return 0 if s > 2**31 else -s
        s = int(str(x)[::-1])
        return 0 if s > 2**31-1 else s
