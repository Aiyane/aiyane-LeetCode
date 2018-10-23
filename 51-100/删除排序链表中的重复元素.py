#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 删除排序链表中的重复元素.py
"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2

示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
"""
__author__ = 'Aiyane'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        v = head.val
        pre = head
        ptr = head.next
        while ptr:
            if ptr.val != v:
                pre.next = ptr
                pre = ptr
                v = pre.val
            else:
                pre.next = None
            ptr = ptr.next
        return head
