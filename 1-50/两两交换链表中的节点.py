#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 两辆交换链表中的节点.py
"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.

说明:
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
"""
思路: 交换指针, 注意链表个数
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        start = head
        h = start.next
        pre = ListNode(0)

        while start:
            end = start.next
            pre.next = end
            if not end:
                pre.next = start
                return h
            nextStart = end.next
            end.next = start
            start.next = nextStart
            pre = start
            start = nextStart
        return h
