#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 完全二叉树的节点个数.py
"""
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入: 
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6
"""
"""
思路：二分法，计算左子树与右子树的高度（遍历左子树计算高度），如果左子树的高度等于右子树，那么返回左边全部节点加上右子树调用
1 << 左子树高度 + countNodes(right)。如果左子树的高度大于右子树，那么返回右子树的全部节点加上左子树调用
1 << 右子树高度 + countNodes(left)。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countDepth(self, root):
        depth = 0
        while root:
            depth += 1
            root = root.left
        return depth

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ld = self.countDepth(root.left)
        rd = self.countDepth(root.right)
        if ld == rd:
            return (1 << ld) + self.countNodes(root.right)
        return (1 << rd) + self.countNodes(root.left)
