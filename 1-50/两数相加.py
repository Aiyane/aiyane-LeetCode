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
        # 保留头节点
        l = l1

        # 不存在 l2
        if not l2:
            return l

        # 不存在 l1
        if not l1:
            return l2

        # 简单相加
        ne, l1.val = divmod(l1.val + l2.val, 10)
        while l1.next and l2.next:
            l1, l2 = l1.next, l2.next
            ne, l1.val = divmod(l1.val + l2.val + ne, 10)

        # 连接
        if l2.next:
            l1.next = l2.next

        # 还有进位
        while l1.next and ne > 0:
            l1 = l1.next
            ne, l1.val = divmod(l1.val + ne, 10)

        # 末尾进位
        if ne:
            l1.next = ListNode(ne)

        return l
