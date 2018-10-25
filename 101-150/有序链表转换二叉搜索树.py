#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 有序链表转换二叉搜索树.py
"""
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:
给定的有序链表： [-10, -3, 0, 5, 9],
一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5
"""
"""
思路：两个指针，一个跳两步，一个跳一步，当跳两步的跳完了，那么跳一步的就到中间节点了。
"""
__author__ = 'Aiyane'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def build_tree(self, head, tail):
        if head == tail:
            return None
        fast = slow = head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        
        root = TreeNode(slow.val)
        root.left = self.build_tree(head, slow)
        root.right = self.build_tree(slow.next, tail)
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        return self.build_tree(head, None)
