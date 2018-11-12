#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 重排链表.py
"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:
给定链表 1->2->3->4, 重新排列为 1->4->2->3.

示例 2:
给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""
__author__ = 'Aiyane'


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None
        ptr = head
        stack = []
        while ptr:
            stack.append(ptr)
            ptr = ptr.next
        left = head
        while 1:
            right = left.next
            cur = stack.pop()
            if cur == left:
                cur.next = None
                return None
            left.next = cur
            if cur == right:
                cur.next = None
                return None
            cur.next = right
            left = right
