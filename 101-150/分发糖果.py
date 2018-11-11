#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 分发糖果.py
"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？


示例 1:
输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。

示例 2:
输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
"""
"""
思路：indexs 中是之前分最多糖果孩子的序号，可能有多个值是因为 1,2,3,4,2,1 这种，4 号孩子分到 4 个糖果，到考察最后一位时，
不能只保存 4 号的位置，应该还保存，4 号孩子分得的糖果数 - 1 这么多个数的 —— 4 号孩子下一个孩子的序号。
"""
__author__ = 'Aiyane'


class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        pre_grade = pre_candy = sum_candy = 0
        indexs = [0]
        for i, cur_grade in enumerate(ratings):
            if cur_grade < pre_grade:
                if pre_candy == 1:
                    sum_candy += i - indexs.pop() if len(indexs) > 1 else i - indexs[-1]
                else:
                    indexs.extend([i for __ in range(1, pre_candy-1)])
            else:
                indexs = [i]

            cur_candy = pre_candy + 1 if cur_grade > pre_grade else 1
            pre_candy, pre_grade = cur_candy, cur_grade
            sum_candy += cur_candy
        return sum_candy
