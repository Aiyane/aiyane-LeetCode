#!/usr/bin/python3
# -*- coding: utf-8 -*-
# File Name: 正则表达式匹配.py
# Created Time: Tue 01 May 2018 07:24:59 PM CST
"""
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
"""
"""
思路: 首先将×*字符组合结合成一个组合, 然后根据每个情况进行划分, 注意递归的条件, 以及局部的优化
"""


class Solution:
    def getRes(self, s, p):
        i = 0
        s_len = len(s)
        p_len = len(p)

        # 局部的优化, 优化最后只剩一个正则字符时, 如果是.*则全匹配, 如果是一般字符且与最后字符不匹配则整个不匹配
        if p_len == 1 and s:
            if p[0][0] == '.' and p[0][1]:
                return True
            elif p[0][0] != '.' and s[-1] != p[0][0]:
                return False

        for si, ch in enumerate(s):
            # 当前有s字符串, 但是p字符串用完了
            if i == p_len:
                return False

            # 如果是'.'字符
            elif p[i][0] == '.':

                # 可以重复
                if p[i][1]:
                    # 观察去掉当前字符可不可以匹配
                    tem = i + 1
                    # 可以匹配直接成功, 不可以匹配就: p字串不变, 先匹配一个字符
                    if tem < p_len and self.getRes(s[si:], p[tem:]):
                        return True
                    else:
                        pass

                # 不是重复的直接考察下一个字符
                else:
                    i += 1

            # 如果是其他字符
            else:

                # 如果该字符不能重复匹配
                if not p[i][1]:
                    # 匹配上了, 考察下一个p字符, 否则失败
                    if p[i][0] == ch:
                        i += 1
                    else:
                        return False

                # 如果是可以重复匹配的
                else:
                    # 如果匹配不上直接匹配下一个字符
                    if ch != p[i][0]:
                        i += 1
                        return self.getRes(s[si:], p[i:])
                    # 否则观察取掉当前字符可不可以匹配, 可以匹配直接成功, 不可以匹配就: p字串不变, 先匹配一个字符
                    else:
                        tem = i + 1
                        if tem < p_len and self.getRes(s[si:], p[tem:]):
                            return True
                        else:
                            pass

        if i == p_len:
            return True
        # 最后没匹配的如果全是x*表达式则匹配, 否则不匹配
        for pch in p[i:]:
            if not pch[1]:
                return False
        return True

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # 构造×*字符组, 与普通字符
        p_list = []
        for ch in p:
            if ch == "*":
                p_list[-1][-1] = True
            else:
                ch_tok = [ch, False]
                p_list.append(ch_tok)

        # 局部优化, 如果正则最后一个字符不是.也不是*表达式,也不与字符串最后一个字符相等, 则不匹配
        if p and s:
            if p_list[-1] and p_list[-1][0] != '.':
                if not p_list[-1][1] and p_list[-1][0] != s[-1]:
                    return False

        # 局部优化, 如果不存在字符串, 判断是否全为*表达式
        if not s:
            for ch in p_list:
                if not ch[1]:
                    return False
            return True

        return self.getRes(s, p_list)
