#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉树的中序遍历.py
"""
给定一个二叉树，返回它的中序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            if root.left:
                res.extend(self.inorderTraversal(root.left))
            res.append(root.val)
            if root.right:
                res.extend(self.inorderTraversal(root.right))
        return res
