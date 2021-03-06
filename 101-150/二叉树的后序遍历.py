#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉树的后序遍历.py
"""
给定一个二叉树，返回它的 后序 遍历。

示例:
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
"""
思路：与前序遍历思路一样，最后再反序就行。
"""
__author__ = 'Aiyane'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        nodes = [root]
        while nodes:
            node = nodes.pop()
            res.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return res[::-1]
