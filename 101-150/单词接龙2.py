#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 单词接龙2.py
"""
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。

说明:
如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
"""
"""
思路：与单词接龙思路差不多，但是需要将每一次的路径记录下来，可以用一个字典来倒序保存上一层的节点。
"""
__author__ = 'Aiyane'


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        wl = len(beginWord)
        begin = {beginWord}
        end = {endWord}
        graph = {beginWord: set()}
        reserve = 1
        while begin and end:
            next_set = set()
            if len(begin) > len(end):
                reserve *= -1
                begin, end = end, begin
            wordList -= begin
            for wd in begin:
                for j in range(wl):
                    for k in range(26):
                        nw = wd[:j] + chr(k+97) + wd[j+1:]
                        if nw in wordList:
                            next_set.add(nw)
                            if reserve == 1:
                                graph.setdefault(nw, set()).add(wd)
                            else:
                                graph.setdefault(wd, set()).add(nw)
            if end & next_set:
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = [[word] + line for line in res if line[0] in graph for word in graph[line[0]]]
                return res
            begin = next_set
        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.findLadders("magic", "pearl", ["flail","halon","lexus","joint","pears","slabs","lorie","lapse","wroth",
    "yalow","swear","cavil","piety","yogis","dhaka","laxer","tatum","provo","truss","tends","deana","dried","hutch",
    "basho","flyby","miler","fries","floes","lingo","wider","scary","marks","perry","igloo","melts","lanny","satan",
    "foamy","perks","denim","plugs","cloak","cyril","women","issue","rocky","marry","trash","merry","topic","hicks",
    "dicky","prado","casio","lapel","diane","serer","paige","parry","elope","balds","dated","copra","earth","marty",
    "slake","balms","daryl","loves","civet","sweat","daley","touch","maria","dacca","muggy","chore","felix","ogled",
    "acids","terse","cults","darla","snubs","boats","recta","cohan","purse","joist","grosz","sheri","steam","manic",
    "luisa","gluts","spits","boxer","abner","cooke","scowl","kenya","hasps","roger","edwin","black","terns","folks",
    "demur","dingo","party","brian","numbs","forgo","gunny","waled","bucks","titan","ruffs","pizza","ravel","poole",
    "suits","stoic","segre","white","lemur","belts","scums","parks","gusts","ozark","umped","heard","lorna","emile",
    "orbit","onset","cruet","amiss","fumed","gelds","italy","rakes","loxed","kilts","mania","tombs","gaped","merge",
    "molar","smith","tangs","misty","wefts","yawns","smile","scuff","width","paris","coded","sodom","shits","benny",
    "pudgy","mayer","peary","curve","tulsa","ramos","thick","dogie","gourd","strop","ahmad","clove","tract","calyx",
    "maris","wants","lipid","pearl","maybe","banjo","south","blend","diana","lanai","waged","shari","magic","duchy",
    "decca","wried","maine","nutty","turns","satyr","holds","finks","twits","peaks","teems","peace","melon","czars",
    "robby","tabby","shove","minty","marta","dregs","lacks","casts","aruba","stall","nurse","jewry","knuth"]))
