#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉树展开为链表.py
"""
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树
    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
"""
思路：构造一个函数，将链表最后一个节点返回，这样就可以用递归解决问题
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def buildList(root):
            node = buildList(root.left) if root.left else root
            if root.left:
                root.right, node.right, root.left = root.left, root.right, None
            return buildList(node.right) if node.right else node
        if root:
            buildList(root)
