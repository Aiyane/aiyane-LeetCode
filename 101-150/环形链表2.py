#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 环形链表2.py
"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

说明：不允许修改给定的链表。

进阶：
你是否可以不用额外空间解决此题？
"""
"""
思路：快慢指针，指向相同节点则将快指针指向头，和慢指针一样一步步后移，会在相交节点相遇。
"""
__author__ = 'Aiyane'


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        loop = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loop = True
                break
        if not loop: return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
