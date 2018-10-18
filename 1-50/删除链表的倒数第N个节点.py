#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 删除链表的倒数第N个节点.py
"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
"""
"""
思路: 一遍扫描, i记录已经扫描几个节点了, 用一个指针p指向目标节点, 当向后遍历时指针也向后移动, 但是i不能增加, 所以i--
如果是头指针, 那么i是小于n的
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = ptr = head
        i = 0
        while ptr.next:
            ptr = ptr.next
            i += 1
            if i == n+1:
                i -= 1
                p = p.next
        if i == n:
            p.next = p.next.next
        else:
            head = head.next
        return head
