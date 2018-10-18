#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# 合并k个排序链表.py
"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""
"""
思路: 将全部指针放入list中, 然后直接使用sort排序, 再重新链接起来
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        nodelist = []
        for head in lists:
            current = head
            while current:
                nodelist.append(current)
                current = current.next

        nodelist.sort(key=lambda x: x.val)

        for i in range(len(nodelist)-1):
            nodelist[i].next = nodelist[i+1]
        if not nodelist:
            return None

        else:
            return nodelist[0]
