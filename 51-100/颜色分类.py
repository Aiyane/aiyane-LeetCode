#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 颜色分类.py
"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

进阶：
一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""
"""
思路：x,y,z指针分别指向0位置起点，1位置起点，2位置起点。那么当当前数字为1时，这时三个指针都需要后移一位，并且将对应位置赋值对应数字。
必须是倒序赋值，但是又要注意当前位置数字不变，也要注意还未开始移动的指针不赋值。
"""
__author__ = 'Aiyane'


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        x = y = z = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                x += 1
                y += 1
                z += 1
                nums[z] = 2
                nums[y] = 1
                nums[x] = 0
            elif nums[i] == 1:
                y += 1
                z += 1
                nums[z] = 2
                if x != -1:
                    nums[x] = 0
                nums[y] = 1
            elif nums[i] == 2:
                z += 1
                if y != -1:
                    nums[y] = 1
                if x != -1:
                    nums[x] = 0
                nums[z] = 2
