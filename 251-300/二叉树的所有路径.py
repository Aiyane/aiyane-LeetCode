#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉树的所有路径.py
"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
输入:
   1
 /   \
2     3
 \
  5


输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        res = []
        if root.left:
            for path in self.binaryTreePaths(root.left):
                res.append(str(root.val) + "->" + path)
        if root.right:
            for path in self.binaryTreePaths(root.right):
                res.append(str(root.val) + "->" + path)
        return res
