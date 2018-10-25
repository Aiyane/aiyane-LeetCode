#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 从中序与后序遍历序列构造二叉树.py
"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
"""
"""
思路：与从前序与中序遍历序列构造二叉树那道题一样的思路，不过是先构造右子树。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        root_val = postorder.pop()
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:])
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        return root
