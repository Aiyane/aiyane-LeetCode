#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 最长公共前缀.py
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""
"""
思路: 注意数组内元素的长度不是数组的长度
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        if not strs:
            return ''
        s_len = min([len(ch) for ch in strs])
        while i < s_len and 1 == len(set([ch[i] for ch in strs])):
            i += 1
        if 0 == i:
            return ''
        return strs[0][:i]


def main():
    s = []
    sol = Solution()
    print(sol.longestCommonPrefix(s))


if __name__ == '__main__':
    main()
