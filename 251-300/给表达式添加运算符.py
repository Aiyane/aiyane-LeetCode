#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 给表达式添加运算符.py
"""
给定一个仅包含数字 0-9 的字符串和一个目标值，在数字之间添加二元运算符（不是一元）+、- 或 * ，返回所有能够得到目标值的表达式。

示例 1:
输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"] 

示例 2:
输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]

示例 3:
输入: num = "105", target = 5
输出: ["1*0+5","10-5"]

示例 4:
输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]

示例 5:
输入: num = "3456237490", target = 9191
输出: []
"""

from operator import add, sub

class Solution:
    def addOperators(self, num: str, target: int):
        res, num_dct = [], {}
        op_dct = {'+': add, '-': sub}

        def cale(prv, num, num_v):
            for i, ch in enumerate(reversed(prv)):
                if ch in op_dct:
                    a, b = prv[:-i-1], prv[-i:]
                    v = num_dct[b+'*'+num] = num_dct[b] * num_v
                    ret = num_dct[a+ch+b+'*'+num] = op_dct[ch](num_dct[a], v)
                    return ret
            ret = num_dct[prv+'*'+num] = num_dct[prv] * num_v
            return ret

        def dfs(prv, beh, ol, prv_l, prv_v):
            num_dct[prv] = prv_v
            if prv_l < ol:
                for i in range(1, ol - prv_l + 1):
                    num = beh[:i]
                    if i == 1 or num[0] != '0':
                        num_v = num_dct[num] = int(num)
                        dfs(prv+'+'+num, beh[i:], ol, prv_l+i, prv_v + num_v)
                        dfs(prv+'-'+num, beh[i:], ol, prv_l+i, prv_v - num_v)
                        dfs(prv+'*'+num, beh[i:], ol, prv_l+i, cale(prv, num, num_v))
            elif prv_v == target:
                res.append(prv)

        l = len(num)
        for i in range(1, l+1):
            prv, beh = num[:i], num[i:]
            if i == 1 or prv[0] != '0':
                prv_v = num_dct[prv] = int(prv)
                dfs(prv, beh, l, i, prv_v)
        return res
