#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 对称二叉树.py
"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:
如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, left, right):
        if left.val != right.val:
            return False
        if left.left and right.right:
            if not self.check(left.left, right.right):
                return False
        elif left.left or right.right:
            return False
        if left.right and right.left:
            if not self.check(left.right, right.left):
                return False
        elif left.right or right.left:
            return False
        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        return self.check(root.left, root.right)
