#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 课程表.py
"""
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例 1:
输入: 2, [[1,0]] 
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

示例 2:
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。

说明:
输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。

提示:
这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 https://www.coursera.org/specializations/algorithms - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。
"""
"""
思路：广度优先：循环删除没有入度的节点以及其关系。如果不存在没有入度的节点，则表示有环。删完了表示没环。
深度优先：先构造图，然后常规思路，记得将结果记录下来。
"""
__author__ = 'Aiyane'

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 广度优先
        if numCourses < 2 or len(prerequisites) < 2:
            return True
        
        while 1:
            count = 0
            mark = [True]*numCourses
            for pre in prerequisites:
                mark[pre[0]] = False
            for pre in prerequisites:
                if mark[pre[1]]:
                    count += 1
                    prerequisites.remove(pre)
            if prerequisites == []:
                return True
            elif count == 0:
                return False
        # 深度优先
        # edge_graph = [[] for i in range(numCourses)]
        # flag_nfs = [0 for i in range(numCourses)]

        # for i, j in prerequisites:
        #     edge_graph[i].append(j)
        
        # def dfs(i):
        #     if flag_nfs[i] == -1:
        #         return False
        #     if flag_nfs[i] == 1:
        #         return True
        #     flag_nfs[i] = -1
            
        #     for j in edge_graph[i]:
        #         if not dfs(j):
        #             return False
                
        #     flag_nfs[i] = 1
        #     return True
        
        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False
        # return True
