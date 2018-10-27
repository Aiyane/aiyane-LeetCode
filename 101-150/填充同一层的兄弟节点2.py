#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 填充同一层的兄弟节点2.py
"""
给定一个二叉树

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

说明:

你只能使用额外常数空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

示例:
给定二叉树，

     1
   /  \
  2    3
 / \    \
4   5    7
调用你的函数后，该二叉树变为：

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL
"""
__author__ = 'Aiyane'


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            ptr = root
            tem = TreeLinkNode(0)
            while ptr:
                if ptr.left:
                    tem.next = ptr.left
                    if ptr.right:
                        tem = ptr.left.next = ptr.right
                    else:
                        tem = ptr.left
                elif ptr.right:
                    tem.next = ptr.right
                    tem = ptr.right
                ptr = ptr.next
            while root:
                if root.left:
                    root = root.left
                    break
                elif root.right:
                    root = root.right
                    break
                root = root.next
