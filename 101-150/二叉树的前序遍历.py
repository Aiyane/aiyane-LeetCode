#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉树的前序遍历.py
"""
给定一个二叉树，返回它的 前序 遍历。

 示例:
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""
"""
思路：使用栈来进行循环遍历。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
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
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)
        return res
