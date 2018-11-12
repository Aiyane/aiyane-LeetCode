#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 逆波兰表达式求值.py
"""
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

示例 1：
输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9

示例 2：
输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6

示例 3：
输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
"""
思路：注意 python 中异号相除与常规思路不一致。
"""
__author__ = 'Aiyane'


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        for num_or_op in tokens:
            if num_or_op not in ('+', '-', '*', '/'):
                nums.append(int(num_or_op))
            else:
                num2 = nums.pop()
                num1 = nums.pop()
                if num_or_op == '+':
                    nums.append(num1 + num2)
                if num_or_op == '-':
                    nums.append(num1 - num2)
                if num_or_op == '*':
                    nums.append(num1 * num2)
                if num_or_op == '/':
                    nums.append(abs(num1) // abs(num2) * -1 if num1*num2 < 0 else num1 // num2)
        return nums.pop()
