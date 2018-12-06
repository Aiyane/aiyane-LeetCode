#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name: 回文数.py
# Created Time: Tue 01 May 2018 07:12:10 PM CST
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true

示例 2:
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？
"""
"""
思路: 取余然后比较, 就可以不转化为字符串
"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        res = 0
        num = x
        while num > 0:
            num, s = divmod(num, 10)
            res = res*10 + s
        return x == res


