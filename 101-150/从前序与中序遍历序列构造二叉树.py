#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 从前序与中序遍历序列构造二叉树.py
"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7
"""
"""
思路：在中序列表中找到前序中的根节点，根节点之前是左树，之后是右树，可以将前序列表之后按照个数切分左右子树，则是一个子问题。
优化：可以将中序列表改成字典 value-index 更快。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        i = inorder.index(rootVal)
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root
