#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 移除链表元素.py
"""
删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""
__author__ = 'Aiyane'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ptr = head
        h = pre = ListNode(0)
        pre.next = ptr
        while ptr:
            if ptr.val == val:
                pre.next = ptr.next
            else:
                pre = ptr
            ptr = ptr.next
        return h.next