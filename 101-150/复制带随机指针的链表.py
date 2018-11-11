#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 复制带随机指针的链表.py
"""
给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的深度拷贝。 
"""
__author__ = 'Aiyane'

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def __init__(self):
        self.map = {}
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head: return None
        if head.label in self.map:
            return self.map[head.label]
        root = RandomListNode(head.label)
        self.map[root.label] = root
        root.next = self.copyRandomList(head.next)
        root.random = self.copyRandomList(head.random) if head.random != head else root
        return root
