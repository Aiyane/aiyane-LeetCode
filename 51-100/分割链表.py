#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 分割链表.py
"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:
输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
"""
__author__ = 'Aiyane'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.val < x:
            pre = pre.next

        end = pre
        mid = ptr = pre.next
        while ptr:
            if ptr.val < x:
                t = pre.next
                pre.next = ptr
                pre = ptr
                n = ptr.next
                ptr.next = t
                ptr = n
            else:
                end.next = ptr
                end = ptr
                ptr = ptr.next
        end.next = None
        return h.next
