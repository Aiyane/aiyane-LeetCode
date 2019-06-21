#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二叉搜索树迭代器.py
"""
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。

注意: next() 和hasNext() 操作的时间复杂度是O(1)，并使用 O(h) 内存，其中 h 是树的高度。
"""
__author__ = 'Aiyane'


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.vals = []
        if root:
            self.start(root)
    
    def start(self, root):
        if root.right:
            self.start(root.right)
        self.vals.append(root.val)
        if root.left:
            self.start(root.left)

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.vals else False

    def next(self):
        """
        :rtype: int
        """
        return self.vals.pop()

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
