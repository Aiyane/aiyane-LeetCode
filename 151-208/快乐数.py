#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 快乐数.py
"""
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 
输入: 19
输出: true
解释: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""
"""
思路：利用集合来保存每一个数字，如果出现循环就返回 False。如果出现 1 返回 True。
"""
__author__ = 'Aiyane'


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        t = 0
        table = set()
        while 1:
            if n == 1:
                return True
            if n in table:
                return False
            table.add(n)
            while n > 0:
                t += (n % 10) * (n % 10)
                n = n // 10
            n = t
            t = 0
