#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name: Z字形变换.py
# Created Time: Tue 01 May 2018 06:03:41 PM CST
"""
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P   A   H   N
A P L S I I G
Y   I   R
之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

string convert(string s, int numRows);
示例 1:

输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"
示例 2:

输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
"""
思路: 构建数组, 将不同组放入不同数组位置
"""
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = ['']*numRows
        i = 0
        j = -1
        for ch in s:
            res[i] += ch
            if i == numRows-1 or i == 0:
                j = -j
            i += j
        return ''.join(res)

