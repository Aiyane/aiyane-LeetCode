#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 报数.py
"""
报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

注意：整数顺序将表示为一个字符串。

示例 1:
输入: 1
输出: "1"

示例 2:
输入: 4
输出: "1211"
"""
"""
思路：常规解法
"""
__author__ = 'Aiyane'


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        res = '11'
        j = 0
        while j < n-2:
            i = 0
            tmp = ''
            while i < len(res):
                p = res[i]
                num = 1
                while i + 1 < len(res) and res[i+1] == p:
                    num += 1
                    i += 1
                i += 1
                tmp += str(num) + p
            res = tmp
            j += 1
        return res
