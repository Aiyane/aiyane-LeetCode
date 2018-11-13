#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 分数到小数.py
"""
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:
输入: numerator = 1, denominator = 2
输出: "0.5"

示例 2:
输入: numerator = 2, denominator = 1
输出: "2"

示例 3:
输入: numerator = 2, denominator = 3
输出: "0.(6)"
"""
"""
思路：如下过程，注意异号单独计算。
##divmod 4/333
# 0, 4
#--------------
##divmod 40/333
# 0, 40
##divmod 400/333
# 1, 67
##divmod 670/333
# 2, 4
##divmod 40/333
################
# 0.(012)
"""
__author__ = 'Aiyane'


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sig = True if numerator * denominator < 0 else False
        numerator = abs(numerator)
        denominator = abs(denominator)
        pre, col = divmod(numerator, denominator)
        if col == 0:
            return '-' + str(pre) if sig else str(pre)
        res = [pre]
        col *= 10
        table = {}
        i = 1
        while col != 0 and col not in table:
            table[col] = i
            pre, col = divmod(col, denominator)
            res.append(pre)
            col *= 10
            i += 1
        if col == 0:
            ans = str(res[0]) + '.' + ''.join([str(num) for num in res[1:]])
        else:
            ans = str(res[0]) + '.' + ''.join([str(num) for num in res[1:table[col]]]) + '(' + ''.join([str(num) for num in res[table[col]:]]) + ')'
        return '-' + ans if sig else ans