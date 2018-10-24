#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 验证二叉搜索树.py
"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, root, minn, maxn):
        v = root.val
        if minn < v < maxn:
            if root.left is None and root.right is None:
                return True
            elif root.left and root.right:
                if self.check(root.left, minn, v) and self.check(root.right, v, maxn):
                    return True
            elif root.left and self.check(root.left, minn, v):
                return True
            elif root.right and self.check(root.right, v, maxn):
                return True
        return False

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        v = root.val
        if root.left and root.right:
            if self.check(root.left, float('-inf'), v) and self.check(root.right, v, float('inf')):
                return True
        elif root.left and self.check(root.left, float('-inf'), v):
            return True
        elif root.right and self.check(root.right, v, float('inf')):
            return True
        return False
