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
思路: sorted是快的, 灵活使用。中位数是左边的数字都小于等于它，右边的数字都大于等于它，那么两个数组是 a，b。
a[i-1] < a[i], b[j-1] < b[j]
a[i-1] < b[j], b[j-1] < a[i]
那么 max(a[i-1], b[j-1]) 与 min(a[i], b[j])中能确定中位数。
首先初始化 i、j。
因为要保证 a[0]...a[i-1] 的个数加 b[0]...b[j-1] 的个数等于 a[i]...a[-1] 的个数加 b[j]...b[-1] 的个数
所以 i 可以定义为 num1 的中位序号，那么 j 就定义为 mid - i。保证 i + j == mid
循环内容就是：
当 a[i-1] > b[j] 时，i += 1 相应由 mid - i 算出 j
当 b[j-1] > a[i] 时，i -= 1 相应由 mid - i 算出 j
直到满足条件为止。
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if len2 < len1:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        mid = (len1 + len2 - 1) >> 1
        start, end = 0, len1
        while start < end:
            i = (start + end) >> 1
            if mid - i - 1 < 0 or nums1[i] >= nums2[mid - i - 1]:
                end = i
            else:
                start = i + 1
        new = sorted(nums1[start:start+2] + nums2[mid-start:mid-start+2])
        return new[0] if (len1 + len2) % 2 != 0 else (new[0]+new[1])/2
