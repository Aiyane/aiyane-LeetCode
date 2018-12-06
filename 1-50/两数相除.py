#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 两数相除.py
"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:
输入: dividend = 10, divisor = 3
输出: 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2

说明:
被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
"""
"""
思路: python大法好啊! 如果不用python, 那么按照手算除法思路, 转成字符串, 然后一个个的移位, 进行相除
"""


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        i = 1
        res = 0
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            i *= -1
        m, n = abs(dividend), abs(divisor)
        while m >= n:
            t = n
            p = 1
            while m > (t<<1):
                t <<= 1
                p <<= 1
            res += p
            m -= t
        return max(min(i*res, 0x7fffffff), -2147483648)
