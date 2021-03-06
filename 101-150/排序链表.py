#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 排序链表.py
"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""
__author__ = 'Aiyane'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        nodes.sort(key=lambda x: x.val)
        head = h = ListNode(0)
        for node in nodes:
            h.next = node
            h = node
        h.next = None
        return head.next
