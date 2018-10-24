#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉树的锯齿形层次遍历.py
"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：
[
  [3],
  [20,9],
  [15,7]
]
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getkid(self, roots, res):
        stack = []
        vals = []
        for root in roots:
            if root.left:
                stack.append(root.left)
                vals.append(root.left.val)
            if root.right:
                stack.append(root.right)
                vals.append(root.right.val)
        if vals:
            if res:
                self.res.append(vals[::-1])
            else:
                self.res.append(vals)
        return stack

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.res = [[root.val]]
        begin = True
        v = self.getkid([root], begin)
        while v:
            begin = not begin
            v = self.getkid(v, begin)
        return self.res
