#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 路径总和2.py
"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
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
    def pathSumDS(self, root, sum, num, nodes):
        if root:
            num += root.val
            if root.left or root.right:
                if root.left:
                    self.pathSumDS(root.left, sum, num, nodes + [root.val])
                if root.right:
                    self.pathSumDS(root.right, sum, num, nodes + [root.val])
            elif num == sum:
                nodes.append(root.val)
                self.res.append(nodes)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.pathSumDS(root, sum, 0, [])
        return self.res