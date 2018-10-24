#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 不同的二叉搜索树2.py
"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:
输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
"""
思路：一个更好的方法应该是用指针，而不是用数组。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def start(self, nums, l):
        if l == 1:
            return [TreeNode(nums[0])]
        if l == 0:
            return []
        res = []
        i = 0
        while i < l:
            kids1 = self.start(nums[:i], i)
            kids2 = self.start(nums[i+1:], l-i-1)
            if kids1 and kids2:
                for v1 in kids1:
                    for v2 in kids2:
                        tree = TreeNode(nums[i])
                        tree.left = v1
                        tree.right = v2
                        res.append(tree)
            elif kids1:
                for v1 in kids1:
                    tree = TreeNode(nums[i])
                    tree.left = v1
                    res.append(tree)
            elif kids2:
                for v2 in kids2:
                    tree = TreeNode(nums[i])
                    tree.right = v2
                    res.append(tree)

            i += 1
        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.start([i for i in range(1, n+1)], n)