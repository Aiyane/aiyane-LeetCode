#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Excel表列名称.py
"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

示例 1:
输入: 1
输出: "A"

示例 2:
输入: 28
输出: "AB"

示例 3:
输入: 701
输出: "ZY"
"""
"""
思路：26 进制，了解 chr 函数的用法，返回 ascii 字符。注意进制转换使用 n - 1去除，因为用 n - 1 时，当 n 为 26 的整除数时，
除数会 -1，余数则为 25。
"""
__author__ = 'Aiyane'


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n:
            n, val = divmod(n-1, 26)
            res = chr(val+65) + res
        return res
