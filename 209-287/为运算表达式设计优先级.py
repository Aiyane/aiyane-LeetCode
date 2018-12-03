#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 为运算表达式设计优先级.py
"""
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:
输入: "2-1-1"
输出: [0, 2]
解释: 
((2-1)-1) = 0 
(2-(1-1)) = 2

示例 2:
输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""
"""
思路：对于存在前后分配重复的组合问题，需要分成前后两个部分，再连接起来。
"""
__author__ = 'Aiyane'


class Solution:
    def operation(self, op, num1, num2):
        if op == '+':
            return num1 + num2
        if op == '-':
            return num1 - num2
        return num1 * num2

    def _diffWaysToCompute(self, nums, ops):
        if not ops:
            return nums
        res = []
        i = 0
        while i < len(ops):
            op = ops[i]
            left = self._diffWaysToCompute(nums[:i+1], ops[:i])
            right = self._diffWaysToCompute(nums[i+1:], ops[i+1:])
            for num1 in left:
                for num2 in right:
                    res.append(self.operation(op, num1, num2))
            i += 1
        return res

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ops = []
        nums = []
        import re
        for m in re.finditer(r'\d+|[-+*]', input):
            tok = m.group(0)
            if tok.isdigit():
                nums.append(int(tok))
            else:
                ops.append(tok)
        return self._diffWaysToCompute(nums, ops)
