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
        if not head:
            return None

        p1 = head
        p0 = None

        while p1.next and p1.next.next:
            p2 = p1.next
            p3 = p2.next

            p2.next = p1
            p1.next = p3

            if p0:
                p0.next = p2
            else:
                head = p2

            p0 = p1
            p1 = p3

        if p1.next:
            p2 = p1.next
            p1.next = None
            p2.next = p1
            if p0:
                p0.next = p2
            else:
                head = p2

        return head
