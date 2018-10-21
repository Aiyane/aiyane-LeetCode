#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文本左右对齐.py
"""
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:
单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。

示例:
输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

示例 2:
输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。

示例 3:
输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""
"""
思路：除最后一个字符的前面全部字符，轮流加一个空格，直到等于 maxWidth 为止。
"""
__author__ = 'Aiyane'
from functools import reduce


class Solution:
    def makeline(self, words, maxWidth):
        wl = len(words) - 1
        if wl == 0:
            return ''.join(words) + ' '*(maxWidth-len(words[0]))
        sl = reduce(lambda x,y:x+y, map(lambda x:len(x), words))
        while 1:
            for i in range(wl):
                words[i] += ' '
                sl += 1
                if sl == maxWidth:
                    return ''.join(words)

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        s = i = 0
        l = len(words)
        maxl = 0
        while i < l:
            wl = len(words[i])+1
            maxl += wl
            if maxl-1 > maxWidth:
                res.append(self.makeline(words[s:i], maxWidth))
                maxl = wl
                s = i
            i += 1
        fin = ' '.join(words[s:])
        res.append(fin + ' '*(maxWidth - len(fin)))
        return res
        
def main():
    sol = Solution()
    print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))

if __name__ == '__main__':
    main()