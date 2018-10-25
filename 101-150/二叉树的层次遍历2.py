#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉树的层次遍历2.py
"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：
[
  [15,7],
  [9,20],
  [3]
]
"""
"""
思路：广度优先遍历。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottomList(self, nodes):
        stack = []
        for node in nodes:
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        if stack:
            self.levelOrderBottomList(stack)
        self.res.append([node.val for node in nodes])
        
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.res = []
        self.levelOrderBottomList([root])
        return self.res
