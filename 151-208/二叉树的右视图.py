#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉树的右视图.py
"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:
输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
"""
思路：深度优先遍历。
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
        self.maxNum = 0
        self.res = []
    
    def rightSideViewDFS(self, root, n):
        if root:
            if n > self.maxNum:
                self.res.append(root.val)
                self.maxNum += 1
            if root.right:
                self.rightSideViewDFS(root.right, n + 1)
            if root.left:
                self.rightSideViewDFS(root.left, n + 1)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.rightSideViewDFS(root, 1)
        return self.res
