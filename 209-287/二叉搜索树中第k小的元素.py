#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉搜索树中第k小的元素.py
"""
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
"""
"""
思路：考察中序遍历，记录序号，如果序号等于k，那么直接返回，否则序号+1，遍历根节点，如果序号等于k返回根节点值，否则遍历右子树。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.index = 0
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0
        res = self.kthSmallest(root.left, k)
        if self.index == k:
            return res
        else:
            self.index += 1
            if self.index == k:
                return root.val
            return self.kthSmallest(root.right, k)
