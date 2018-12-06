#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 合并两个有序链表.py
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
"""
思路: 三个关键指针, pi指向l1, pj指向l2, ptr指向合并的链表, p表示合并的链表的头节点, 可能是l1也可能是l2.
ptr在l1与l2之间跳转, pi与pj始终领先ptr指针一个位置, pi和pj哪个先指向了None就要合并另一个指针指向的链表.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 首先判断是否为空链表
        if not l1:
            return l2
        elif not l2:
            return l1
        
        pi, pj = l1, l2
        h = p = ListNode(-1)
        while pi and pj:
            if pi.val <= pj.val:
                p.next, p, pi = pi, pi, pi.next
            else:
                p.next, p, pj = pj, pj, pj.next
        if pi:
            p.next = pi
        elif pj:
            p.next = pj
        return h.next
