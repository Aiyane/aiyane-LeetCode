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

        # 初始化变量
        pi = l1
        pj = l2
        p = ptr = None

        while True:
            if pi.val >= pj.val:
                # 如果有ptr, 表示结果链表已经存在
                # 那么移动是需要先将ptr的next指向pj
                # 因为现在pj的值是比pi的值小
                # 那么ptr首先应该链接pj
                # 如果ptr不存在, 表示现在是第一次比较
                # 这是ptr逻辑上其实就是l2的开始, 即pj节点
                # 因为pj的移动ptr也会改变, 所以只需要在最后做赋值即可
                if ptr:
                    ptr.next = pj

                # 由于只有next指针, 所以需要一个tem指针保存
                # 刚好小于或等于pi节点值的节点指针, pj则指向刚好大于pi的节点
                while pi.val >= pj.val:
                    tem = pj
                    pj = pj.next

                    # 如果循环完全部l2链表, 那么就可以判断最后一个节点为tem
                    # 让tem指向pi这个大于它的节点就可以直接返回头指针p或者l2
                    if pj is None:
                        tem.next = pi
                        return p if p else l2

                # 刚好小于pi的节点的next指向pi
                # 现在结果链表ptr移到pi处, pi应该指向它的下一个节点
                tem.next = pi
                ptr = pi
                pi = pi.next

                # 这里如果l1(pi)已经遍历完, 那么ptr的下一个节点就是pj
                # 直接连接pj返回结果的头指针
                if pi is None:
                    ptr.next = pj
                    return p if p else l2

                # 如果是第一次比较, 头指针p就应该为l2
                if p is None:
                    p = l2

            else:
                if ptr:
                    ptr.next = pi

                while pi.val <= pj.val:
                    tem = pi
                    pi = pi.next

                    if pi is None:
                        tem.next = pj
                        return p if p else l1

                tem.next = pj
                ptr = pj
                pj = pj.next

                if pj is None:
                    ptr.next = pi
                    return p if p else l1

                if p is None:
                    p = l1
