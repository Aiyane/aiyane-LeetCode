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
"""
prv_str: 前缀串
op: 操作符
prv_op: 操作符函数
prv_num: 前缀后一个字符
beh_str: 后缀字符串
ol: 初始数字长度
prv_str_add_num_l: 前缀加前缀后一个字符的总长度
prv_num_l: 前缀后一个字符的长度
prv_str_v: 前缀串的计算值
prv_num_v: 前缀后一个字符的值
"""


class Solution:
    def addOperators(self, num: str, target: int):
        ol, res = len(num), []

        def dfs(prv_str, op, prv_op, prv_num, beh_str, prv_str_add_num_l, prv_num_l, prv_str_v, prv_num_v):
            new_prv_str_v = prv_op(prv_str_v, prv_num_v)
            new_prv_str = prv_str + op + prv_num
            if prv_str_add_num_l < ol:
                for i in range(1, ol - prv_str_add_num_l + 1):
                    new_prv_num, new_beh_str = beh_str[:i], beh_str[i:]
                    if i == 1 or new_prv_num[0] != '0': 
                        new_prv_num_v = int(new_prv_num)
                        dfs(new_prv_str, '+', lambda x, y: x + y, new_prv_num, new_beh_str, prv_str_add_num_l + i, i, new_prv_str_v, new_prv_num_v)
                        dfs(new_prv_str, '-', lambda x, y: x - y, new_prv_num, new_beh_str, prv_str_add_num_l + i, i, new_prv_str_v, new_prv_num_v)
                        dfs(prv_str, op, prv_op, prv_num + '*' + new_prv_num, new_beh_str, prv_str_add_num_l + i, prv_num_l + i, prv_str_v, prv_num_v * new_prv_num_v)
            elif new_prv_str_v == target:
                res.append(new_prv_str)

        for i in range(1, ol+1):
            prv, beh = num[:i], num[i:]
            if i == 1 or prv[0] != '0':
                prv_v = int(prv)
                dfs('', '', lambda x, y: y, prv, beh, i, i, 0, prv_v)
        return res
