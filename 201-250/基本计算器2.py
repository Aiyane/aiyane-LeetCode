#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 基本计算器2.py
"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:
输入: "3+2*2"
输出: 7

示例 2:
输入: " 3/2 "
输出: 1

示例 3:
输入: " 3+5 / 2 "
输出: 5

说明：
你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
"""
__author__ = 'Aiyane'


class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = []
        ops = []
        i = num = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = int(ch)
                while i + 1 < len(s) and s[i+1].isdigit():
                    i += 1
                    ch = s[i]
                    num = num * 10 + int(ch)
                nums.append(num)
                num -= num
                if ops and ops[-1] in ('*', '/'):
                    if ops[-1] == '*':
                        op = ops.pop()
                        num2 = nums.pop()
                        num1 = nums.pop()
                        nums.append(num1 * num2)
                    elif ops[-1] == '/':
                        op = ops.pop()
                        num2 = nums.pop()
                        num1 = nums.pop()
                        nums.append(num1 // num2)
            elif ch == '+' or ch == '-':
                if ops:
                    op = ops.pop()
                    num2 = nums.pop()
                    num1 = nums.pop()
                    nums.append(num1 + num2 if op == '+' else num1 - num2)
                ops.append(ch)
            elif ch == '*' or ch == '/':
                ops.append(ch)
            i += 1
        while ops:
            op = ops.pop()
            num2 = nums.pop()
            num1 = nums.pop()
            nums.append(num1 + num2 if op == '+' else num1 - num2)
        return nums.pop()
