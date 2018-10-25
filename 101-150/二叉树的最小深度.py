#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉树的最小深度.py
"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。

示例:
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepthWS(self, nodes, num):
        stack = []
        for node in nodes:
            if node.left or node.right:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            else:
                return num+1
        return self.minDepthWS(stack, num+1)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.minDepthWS([root], 0)
