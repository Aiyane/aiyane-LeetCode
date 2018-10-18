# -*- coding: utf-8 -*-
#!/usr/bin/python3
# File Name: 两数相加.py
# Created Time: Sun 29 Apr 2018 11:14:52 PM CST
"""
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""
"""
思路: 只改一个链表, 只改指针, 知道divmod的用法
"""
#  Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ne = 0
        l = l1
        while True:
            l1.val += ne
            ne, l1.val = divmod(l1.val + l2.val, 10)
            if l1.next is None or l2.next is None:
                break
            l1 = l1.next
            l2 = l2.next
        if l2.next:
            l1.next = l2.next
        if l1.next and ne:
            l1 = l1.next
            while l1:
                l1.val += ne
                ne, l1.val = divmod(l1.val, 10)
                if not l1.next:
                    break
                l1 = l1.next
        if ne:
            l1.next = ListNode(ne)
        return l

