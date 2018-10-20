#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 旋转链表.py
"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL

解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL

解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""
"""
思路：注意节点个数，注意旋转次数取余
"""
__author__ = 'Aiyane'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        if head.next.next is None:
            if k % 2 == 0:
                return head
            e = head.next
            e.next = head
            head.next = None
            return e

        e = head
        old = None
        s = 1
        while e.next:
            s += 1
            old = e
            e = e.next
        k = k % s
        
        while k > 0:
            old.next = None
            e.next = head
            while head.next != old:
                head = head.next
            old = head
            head = e
            e = old.next
            k -= 1
        return head
        