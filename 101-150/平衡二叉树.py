#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 平衡二叉树.py
"""
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def treeHeight(self, root, height):
        left_h = self.treeHeight(root.left, height+1) if root.left else height
        right_h = self.treeHeight(root.right, height+1) if root.right else height
        if left_h and right_h and -1 <= left_h - right_h <= 1:
            return max(left_h, right_h)
        return False

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if self.treeHeight(root, 1):
            return True
        return False
