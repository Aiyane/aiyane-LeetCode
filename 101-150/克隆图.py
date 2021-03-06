#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 克隆图.py
"""
克隆一张无向图，图中的每个节点包含一个 label （标签）和一个 neighbors （邻接点）列表 。

OJ的无向图序列化：

节点被唯一标记。

我们用 # 作为每个节点的分隔符，用 , 作为节点标签和邻接点的分隔符。

例如，序列化无向图 {0,1,2#1,2#2,2}。
该图总共有三个节点, 被两个分隔符  # 分为三部分。 
第一个节点的标签为 0，存在从节点 0 到节点 1 和节点 2 的两条边。
第二个节点的标签为 1，存在从节点 1 到节点 2 的一条边。
第三个节点的标签为 2，存在从节点 2 到节点 2 (本身) 的一条边，从而形成自环。
我们将图形可视化如下：

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""
"""
思路：深度优先遍历，记得要保存节点。
"""
__author__ = 'Aiyane'


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def __init__(self):
        self.nodes = {}
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        if node.label in self.nodes:
            return self.nodes[node.label]
        root = UndirectedGraphNode(node.label)
        self.nodes[node.label] = root
        root.neighbors = [self.cloneGraph(next_node) for next_node in node.neighbors]
        return root
