#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉树的层次遍历.py
"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：
[
  [3],
  [9,20],
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
    def getkid(self, roots):
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
            self.res.append(vals)
        return stack

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.res = [[root.val]]
        v = self.getkid([root])
        while v:
            v = self.getkid(v)
        return self.res
