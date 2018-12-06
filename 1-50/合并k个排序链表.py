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
思路: 将全部指针放入list中, 然后直接使用sort排序, 再重新链接起来。或者使用堆
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def heappush(heap, item):
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos][0] < heap[rightpos][0]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


def heappop(heap):
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem[0] < parent[0]:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for head in lists:
            if head:
                heappush(heap, (head.val, head))
        h = p = ListNode(-1)
        while heap:
            val, node = heappop(heap)
            p.next = node
            p = node
            if node.next:
                heappush(heap, (node.next.val, node.next))
        return h.next
