#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 与所有单词相关联的字串.py
"""
给定一个字符串 s 和一些长度相同的单词 words。在 s 中找出可以恰好串联 words 中所有单词的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1:
输入:
  s = "barfooothefooobarman",
  words = ["fooo","bar"]

输出: [0,9]

解释: 从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

示例 2:
输入:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]

输出: []
"""
"""
思路：构造单词字典，因为长度是一样的，所以大循环里只需要循环min(width, length_s - length_words + 1)
如果获取的单词比结果还多，从第一个单词开始去掉，直到符合结果
"""
import profile


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        length_s = len(s)
        width = len(words[0])
        length_words = len(words)*width
        if length_s < length_words:
            return []

        result = []

        # 首先构造单词表次数字典
        times = dict()
        for word in words:
            if word not in times:
                times[word] = 1
            else:
                times[word] += 1

        # 按照单词长度遍历，所以从单词长度开始重复，或者字符串长度减去单词长度即可
        ll = min(width, length_s - length_words + 1)
        for i in range(ll):
            s_start, s_end = i, i
            d = dict()
            while s_start + width <= length_s:
                word = s[s_end:s_end+width]
                s_end += width
                if word not in times:
                    s_start = s_end
                    d.clear()
                    # 如果长度不够，提前结束
                    if length_s - s_start < length_words:
                        break

                else:
                    if word not in d:
                        d[word] = 1
                    else:
                        d[word] += 1

                    # 如果获取的单词比结果还多，从第一个单词开始去掉，直到符合结果
                    while d[word] > times[word]:
                        d[s[s_start:s_start+width]] -= 1
                        s_start += width

                    if s_end - s_start == length_words:
                        result.append(s_start)
        return result


def main():
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    # s = "barfoothefoobarman"
    # words = ["foo", "bar"]
    sol = Solution()
    print(sol.findSubstring(s, words))


if __name__ == '__main__':
    profile.run('main()')
