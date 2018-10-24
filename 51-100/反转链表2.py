#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 反转链表2.py
"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""
__author__ = 'Aiyane'


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        res = []
        start = ptr = h = ListNode(0)
        h.next = head
        i = 0
        while True:
            ptr = ptr.next
            i += 1
            if i == n:
                end = ptr.next
                res.append(ptr)
                break
            elif i >= m:
                res.append(ptr)
            else:
                start = ptr
        while res:
            node = res.pop()
            start.next = node
            start = node
        start.next = end
        return h.next
