# -*- coding: utf-8 -*-
#!/usr/bin/python3
# File Name: 两个排序数组的中位数.py
# Created Time: Mon 30 Apr 2018 01:10:55 AM CST
"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
"""
"""
思路: sorted是快的, 灵活使用
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n_len = len(nums1) + len(nums2)
        if not nums1 and not nums2:
            return 0
        if not nums1:
            nums1 = nums2
        else:
            nums1.extend(nums2)
            nums1 = sorted(nums1)
        mid = n_len//2
        if n_len%2 == 1:
            return nums1[mid]
        else:
            return (nums1[mid] + nums1[mid-1])/2
