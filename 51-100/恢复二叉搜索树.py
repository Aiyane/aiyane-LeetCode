#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 恢复二叉搜索树.py
"""
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:
输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2

示例 2:
输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

进阶:
使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？
"""
"""
思路：如果发现哪个节点有错，则返回那个节点，上一层获得该节点，交换节点的值，再将该节点作为参数递归调用。
"""
__author__ = 'Aiyane'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find(self, root, minn, maxn):
        v = root.val
        if minn < v < maxn:
            if root.left:
                node = self.find(root.left, minn, v)
                if node:
                    if minn < node.val < maxn:
                        root.val = node.val
                        node.val = v
                        return self.find(root, minn, maxn)
                    return node
            if root.right:
                node = self.find(root.right, v, maxn)
                if node:
                    if minn < node.val < maxn:
                        root.val = node.val
                        node.val = v
                        return self.find(root, minn, maxn)
                    return node
        else:
            return root

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.find(root, float('-inf'), float('inf'))
