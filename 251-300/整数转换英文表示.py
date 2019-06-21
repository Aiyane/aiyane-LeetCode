#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 整数转换英文表示.py
"""
将非负整数转换为其对应的英文表示。可以保证给定输入小于 231 - 1 。

示例 1:
输入: 123
输出: "One Hundred Twenty Three"

示例 2:
输入: 12345
输出: "Twelve Thousand Three Hundred Forty Five"

示例 3:
输入: 1234567
输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

示例 4:
输入: 1234567891
输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        num1_9 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        num10_19 = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        num20_90 = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        def help(n):
            if num == 0:
                return 'Zero'
            res = ""
            if n < 10:
                return num1_9[n]
            if n < 20:
                return num10_19[n-10]
            if n < 100:
                a, b = divmod(n, 10)
                if b > 0:
                    return num20_90[a] + ' ' + num1_9[b]
                return num20_90[a]
            if n < 1000:
                a, b = divmod(n, 100)
                if b > 0:
                    return help(a) + " Hundred " + help(b)
                return help(a) + " Hundred"
            if n < 1000000:
                a, b = divmod(n, 1000)
                if b > 0:
                    return help(a) + " Thousand " + help(b)
                return help(a) + " Thousand"
            if n < 1000000000:
                a, b = divmod(n, 1000000)
                if b > 0:
                    return help(a) + " Million " + help(b)
                return help(a) + " Million"
            a, b = divmod(n, 1000000000)
            if b > 0:
                return help(a) + " Billion " + help(b)
            return help(a) + " Billion"
        return help(num)
            