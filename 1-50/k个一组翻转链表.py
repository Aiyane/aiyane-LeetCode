#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# k个一组翻转链表.py
"""
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
"""
思路: k个变量放在一个数组中, 每次装满数组就将它们倒着连起来, 装不满就连第一个, 最后返回
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        ps = [None]*k
        p0 = ListNode(0)
        head = p0
        i = 0
        while p:
            ps[i] = p
            p = p.next
            i += 1
            if i == k:
                i = 0
                for pi in ps[::-1]:
                    p0.next = pi
                    p0 = pi
                ps = [None]*k
                p0.next = None
        p0.next = ps[0]
        return head.next
