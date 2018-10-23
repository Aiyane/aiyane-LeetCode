#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 删除排序链表中的重复元素2.py
"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5

示例 2:
输入: 1->1->1->2->3
输出: 2->3
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
        res = []
        jump = False
        while head.next:
            if head.next.val != v:
                if not jump:
                    res.append(head)
                v = head.next.val
                jump = False
            else:
                jump = True
            head = head.next
        if not jump:
            res.append(head)
        if not res:
            return None
        h = res[0]
        h.next = None
        for node in res[1:]:
            h.next = node
            h = node
            node.next = None
        return res[0]
