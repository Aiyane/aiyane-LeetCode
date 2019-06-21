#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 买卖股票的最佳时机4.py
"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2:
输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
"""
"""
思路：结合 2、3 中的例子，在 2 中由于交易次数足够大，那么一次遍历搞定。在 3 中，交易次数过少，则两层循环解决。
"""
__author__ = 'Aiyane'


class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) // 2 <= k:
            maxnum = 0
            for i, v in enumerate(prices[1:]):
                if prices[i] < v:
                    maxnum += v - prices[i]
            return maxnum
        else:
            res = [float('-inf') if i % 2 == 0 else 0 for i, __ in enumerate(range(k*2))]
            for price in prices:
                for i, p in enumerate(res):
                    if i % 2 == 0:
                        if i == 0:
                            if res[i] < -price:
                                res[i] = -price
                        elif res[i] < -price + res[i-1]:
                            res[i] = -price + res[i-1]
                    elif res[i] < price + res[i-1]:
                        res[i] = price + res[i-1]
            return res.pop() if res else 0
