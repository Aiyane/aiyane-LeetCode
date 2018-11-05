#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 环形链表.py
"""
给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？
"""
"""
思路：跳一步与跳两步，有环的话早晚相遇。
"""
__author__ = 'Aiyane'


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        pre = net = head
        while pre.next and net.next and net.next.next:
            net = net.next.next
            pre = pre.next
            if pre == net:
                return True
        return False
