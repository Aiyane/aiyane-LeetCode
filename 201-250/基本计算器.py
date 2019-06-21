#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 基本计算器.py
"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:
输入: "1 + 1"
输出: 2

示例 2:
输入: " 2-1 + 2 "
输出: 3

示例 3:
输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23

说明：
你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
"""
"""
思路：使用栈。
"""
__author__ = 'Aiyane'


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        ops = []
        nums = []
        for m in re.finditer(r'\d+|[-+()]', s):
            token = m.group(0)
            if token.isdigit():
                if ops and ops[-1] != '(':
                    op = ops.pop()
                    num1 = nums.pop()
                    if op == '+':
                        nums.append(num1 + int(token))
                    elif op == '-':
                        nums.append(num1 - int(token))
                else:
                    nums.append(int(token))
            elif token == '+' or token == '-' or token == '(':
                ops.append(token)
            elif token == ')':
                op = ops.pop()
                while op != '(':
                    num2 = nums.pop()
                    num1 = nums.pop()
                    if op == '+':
                        nums.append(num1 + num2)
                    elif op == '-':
                        nums.append(num1 - num2)
                    op = ops.pop()
                if ops and ops[-1] != '(':
                    op = ops.pop()
                    num2 = nums.pop()
                    num1 = nums.pop()
                    if op == '+':
                        nums.append(num1 + num2)
                    elif op == '-':
                        nums.append(num1 - num2)
        return nums.pop()
