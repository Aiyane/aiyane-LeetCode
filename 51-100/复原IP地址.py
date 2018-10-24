#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 复原IP地址.py
"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""
"""
思路：回溯法，注意每段不大于255，每段长度大于1的不以0开头。
"""
__author__ = 'Aiyane'


class Solution:
    def start(self, s, n, l):
        if l > n*3:
            return []
        if l < n:
            return []
        if l == n:
            return ['.'.join(list(s))]
        if n == 1:
            if l > 1 and s[0] == '0':
                return []
            if int(s) > 255:
                return []
            return [s]
        res = []
        for i in range(1, 4):
            if i > 1 and s[0] == '0':
                break
            if int(s[:i]) <= 255:
                tem = self.start(s[i:], n-1, l-i)
                if tem:
                    for t1 in tem:
                        res.append(s[:i] + '.' + t1)
        return res

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.start(s, 4, len(s))