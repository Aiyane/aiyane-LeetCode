#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 天际线问题.py
"""
城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。现在，假设您获得了城市风光照片（图A）上显示的所有建筑物的位置和高度，
请编写一个程序以输出由这些建筑物形成的天际线（图B）。

https://leetcode-cn.com/problems/the-skyline-problem/
Buildings  Skyline Contour
每个建筑物的几何信息用三元组 [Li，Ri，Hi] 表示，其中 Li 和 Ri 分别是第 i 座建筑物左右边缘的 x 坐标，Hi 是其高度。
可以保证 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX 和 Ri - Li > 0。您可以假设所有建筑物都是在绝对平坦且高度为 0 的表面上的完美矩形。

例如，图A中所有建筑物的尺寸记录为：[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 。

输出是以 [ [x1,y1], [x2, y2], [x3, y3], ... ] 格式的“关键点”（图B中的红点）的列表，它们唯一地定义了天际线。
关键点是水平线段的左端点。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

例如，图B中的天际线应该表示为：[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]。

说明:
任何输入列表中的建筑物数量保证在 [0, 10000] 范围内。
输入列表已经按升序排列在左边的 x 位置 Li 。
输出列表必须按 x 位排序。
输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；
三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
"""
"""
思路：使用大根堆来解决，大厦的左节点与右节点进行全部排序，如果是左节点，就放入堆中，如果是右节点，就将堆中的该节点对应的左节点删除。
一直要保持堆的结构，然后从堆中取出当前最大的高度，如果最大的高度与上一次的最大高度一样，那么忽略。如果不一样了，就把该节点添加到结果。
"""
__author__ = 'Aiyane'


class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        from heapq import heappush, heappop

        if not buildings:
            return buildings

        points = []
        for l, r, h in buildings:
            points.append((l, -h))
            points.append((r, h))

        points.sort()

        result = []
        heights = [0]
        prev = heights[0]

        ignored = defaultdict(int)

        for x, h in points:
            if h < 0:
                heappush(heights, h)
            else:
                ignored[-h] += 1

            # 由于heappop只能一次移除最小的元素，所以先保存应当移除的元素，等到该元素成为最小元素时，就把该元素移除。
            # 或者使用
            # # 找到 h 的序号 i
            # i = heap.index(-h)
            # heights[i] = heights[-1]
            # # 把第 h 删除，但是最后一个元素现在在 i 号位置
            # heights.pop()
            # # 这里如果 i 就是最后一个元素则不需要重新排序
            # if i < len(heap):
            #     # 第 i 号元素考察父节点们，进行交换
            #     heapq._siftup(heights, i)
            #     # 考察第 i 号元素子节点们，进行交换
            #     heapq._siftdown(heights, 0, i)
            while ignored[heights[0]] > 0:
                ignored[heights[0]] -= 1
                heappop(heights)

            cur = heights[0]
            if cur != prev:
                result.append((x, -cur))
                prev = cur

        return result
