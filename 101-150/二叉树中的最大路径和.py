#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉树中的最大路径和.py
"""
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:
输入: [1,2,3]

       1
      / \
     2   3

输出: 6

示例 2:
输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7
输出: 42
"""
"""
思路：首先我们分析一下对于指定某个节点为根时，最大的路径和有可能是哪些情况。
第一种是左子树的路径加上当前节点，
第二种是右子树的路径加上当前节点，
第三种是左右子树的路径加上当前节点（相当于一条横跨当前节点的路径），
第四种是只有自己的路径。乍一看似乎以此为条件进行自下而上递归就行了，
然而这四种情况只是用来计算以当前节点根的最大路径，如果当前节点上面还有节点，
那它的父节点是不能累加第三种情况的。所以我们要计算两个最大值，一个是当前节点下最大路径和，
另一个是如果要连接父节点时最大的路径和。我们用前者更新全局最大量，用后者返回递归值就行了。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def currPathSum(self, root):
        if root is None:
            return 0
        left = self.currPathSum(root.left)
        right = self.currPathSum(root.right)
        currSum = max(root.val, right + root.val, left + root.val)
        currMax = max(currSum,  root.val + left + right)
        if self.maxVal < currMax:
            self.maxVal = currMax
        return currSum

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxVal = float('-inf')
        self.currPathSum(root)
        return self.maxVal
