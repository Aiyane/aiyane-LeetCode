#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 回文链表.py
"""
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
"""
思路：考虑翻转后半段链表，翻转链表的实现方式使用递归实现。然后使用快慢指针来找出中间节点。
"""
__author__ = 'Aiyane'


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverse(self, node):
        if not node or not node.next:
            return node
        newNode = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return newNode

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        slow = self.reverse(slow.next)
        while slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
