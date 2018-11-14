#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 颠倒二进制位.py
"""
颠倒给定的 32 位无符号整数的二进制位。

示例:
输入: 43261596
输出: 964176192
解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
     返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
进阶:
如果多次调用这个函数，你将如何优化你的算法？
"""
__author__ = 'Aiyane'

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        str_num = bin(n)[2:]
        return int(('0'*(32 - len(str_num)) + str_num)[::-1], 2)
