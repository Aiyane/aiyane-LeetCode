#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 比较版本号.py
"""
比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

你可以假设版本字符串非空，并且只包含数字和 . 字符。

 . 字符不代表小数点，而是用于分隔数字序列。

例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。

示例 1:
输入: version1 = "0.1", version2 = "1.1"
输出: -1

示例 2:
输入: version1 = "1.0.1", version2 = "1"
输出: 1

示例 3:
输入: version1 = "7.5.2.4", version2 = "7.5.3"
输出: -1
"""
__author__ = 'Aiyane'


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) > len(v2):
            for i, v in enumerate(v2):
                if int(v1[i]) > int(v):
                    return 1
                if int(v1[i]) < int(v):
                    return -1
            for v in v1[i+1:]:
                if 0 < int(v):
                    return 1
            return 0
        elif len(v1) < len(v2):
            for i, v in enumerate(v1):
                if int(v2[i]) > int(v):
                    return -1
                if int(v2[i]) < int(v):
                    return 1
            for v in v2[i+1:]:
                if 0 < int(v):
                    return -1
            return 0
        else:
            for v_1, v_2 in zip(v1, v2):
                if int(v_1) > int(v_2):
                    return 1
                if int(v_1) < int(v_2):
                    return -1
            return 0